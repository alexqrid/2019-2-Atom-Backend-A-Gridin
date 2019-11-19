from django.db.models import Max
from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponseRedirect
from .models import Chat, Member, Message
from users.models import User
from .forms import ChatCreateForm, CreateMessageForm
from .utils import chat_exists


@require_http_methods(['GET', 'POST'])
def chat_list(request):
    """ Returns all chats list"""
    # try:
    #     user = User.objects.get(username=request.GET['username'])
    # except User.DoesNotExist:
    #     return JsonResponse({"Error": "User does not exists"}, status=404)
    # chats = Member.objects.select_related('Chat').filter(user_id=user)
    chats = {'chats': []}

    for i in Chat.objects.all():
        chats['chats'].append({
            "id": i.id,
            "title": i.title,
            "description": i.description,
            "Is group?": i.is_group,
            "participants":
                [j.user.username for j in Member.objects.filter(chat=i.id).select_related('user')]
        }
        )
    return JsonResponse(chats)


@require_http_methods(['GET', 'POST'])
def chat(request, chat_id):
    """ Return chat specified by id
    and all messages in the chat"""
    _chat = get_object_or_404(Chat, id=chat_id)
    messages = Message.objects.select_related('chat', 'user').filter(chat=_chat).order_by('id')
    mesg = []
    for i in messages:
        mesg.append({"id": i.id,
                     "sender": i.user.username,
                     "Message": i.content,
                     "Date": i.created_at
                     })
    return JsonResponse({
        "Title": _chat.title,
        "Description": _chat.description,
        "Is group": _chat.is_group,
        "messages": mesg
    })


@require_http_methods(["GET", 'POST'])
def hello(request, name="Stranger"):
    return render(request, 'Hello.html', {'name': name, 'links': ['create message', 'list', 'contacts']})


@require_http_methods(['POST'])
@csrf_exempt
def create_chat(request):
    """Chat creation using POST request"""
    owner = request.POST['from']
    to = request.POST['to']
    try:
        user = User.objects.get(username=owner)
        acceptor = User.objects.get(username=to)
    except User.DoesNotExist:
        return JsonResponse({"Error": "User does not exists"}, status=404)
    new_chat = Chat()
    new_chat.title = request.POST['title']
    desc = request.POST['description']
    if desc:
        new_chat.description = desc
    new_chat.save()
    Member.objects.create(user=user, chat=new_chat)
    Member.objects.create(user=acceptor, chat=new_chat)
    return JsonResponse({"description": "You have successfully created new chat"}, status=200)


@csrf_exempt
def new_chat(request):
    """ Chat creation using form"""
    form = ChatCreateForm(request.POST or None)
    if form.is_valid():
        sender = User.objects.get(username=form['sender'].value())
        recipient = User.objects.get(username=form['recipient'].value())
        existed = chat_exists(sender, recipient)
        if existed:
            """ If chat between two users already exists
            we need to update values in Member model and
            add message to Message model """
            chat = Chat.objects.get(id=existed[0])
            msg = Message.objects.create(content=form['message'].value(),
                                         user=sender,
                                         chat=chat)
            Member.objects.filter(user=sender,
                                  chat=chat).update(
                last_msg=msg)
            Member.objects.filter(user=recipient,
                                  chat=chat).update(
                new_msg=True)
        else:
            """ If chat between two users does not exist
            we have to create it and fill appropriate models """
            chat = Chat.objects.create(title=form['title'].value(),
                                       description=form['description'].value())
            msg = Message.objects.create(content=form['message'].value(),
                                         user=sender,
                                         chat=chat)
            Member.objects.create(user=sender, chat=chat,
                                  new_msg=False, last_msg=msg)
            Member.objects.create(user=recipient, chat=chat, new_msg=True)
        return redirect('chat', chat_id=chat.id)
    return render_to_response('chat.html', {"form": form})


@csrf_exempt
def send_message(request, chat_id):
    """ Creates message in a specified chat"""
    chat = get_object_or_404(Chat, id=chat_id)
    form = CreateMessageForm(request.POST or None)
    if form.is_valid():
        sender = User.objects.get(id=form["user"].value())
        try:
            Member.objects.get(user=sender, chat=chat_id)
        except Member.DoesNotExist:
            return JsonResponse({"Error": "This user is not allowed to send message to this chat"}, status=403)
        msg = Message.objects.create(user=sender,
                                     chat=chat,
                                     content=form['content'].value())
        Member.objects.filter(chat=chat).exclude(user=sender).update(new_msg=True)
        Member.objects.filter(user=sender, chat=chat).update(last_msg=msg, new_msg=False)
        return redirect("chat", chat_id=chat_id)
    return render_to_response('message.html', {"form": form})


def read_message(request, chat_id, username):
    if not Member.objects.filter(chat=chat_id, user=User.objects.get(username=username)).exists():
        return JsonResponse({"Error": f"User\'{username}\' is not a member of the chat"},
                            status=404)
    msg = Member.objects.filter(chat=chat_id).aggregate(Max('last_msg'))['last_msg__max']
    Member.objects.filter(chat=chat_id,
                          user=User.objects.get(username=username)
                          ).update(new_msg=False,
                                   last_msg=msg)
    return redirect("chat", chat_id=chat_id)
