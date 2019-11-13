from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import Chat, Member
from users.models import User


@require_http_methods(['GET', 'POST'])
def chat_list(request):
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
            "description": i.description
        }
        )
    return JsonResponse(chats)


@require_http_methods(['GET', 'POST'])
def chat(request):
    return JsonResponse({
        "last_messages_count": 10,
        "last_message_id": 103,
        "opponent_id": 2
    })


@require_http_methods(["GET", 'POST'])
def hello(request, name="Stranger"):
    return render(request, 'Hello.html', {'name': name, 'links': ['chat', 'list', 'contacts']})


@require_http_methods(['POST'])
@csrf_exempt
def create_chat(request):
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
    Member.objects.create(user_id=user, chat_id=new_chat)
    Member.objects.create(user_id=acceptor, chat_id=new_chat)
    return JsonResponse({"description": "You have successfully created new chat"}, status=200)
