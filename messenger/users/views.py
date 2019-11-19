from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from .models import User
from chats.models import Chat, Member


@require_http_methods(['GET', 'POST'])
def profile(request, username):
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        return JsonResponse({"Error": "User does not exists"}, status=404)
    messages = Member.objects.filter(user=user, new_msg=True)
    mesg = []
    for i in messages:
        mesg.append({"chat_id": i.chat.id})
    return JsonResponse({
        'username': user.username,
        'First name': user.first_name,
        'Last name': user.last_name,
        'e-mail': user.email,
        'phone': user.phone_number,
        "Creation date": user.date_joined,
        "Notifications": [{"New messages": mesg}]
    })


@require_http_methods(['GET', 'POST'])
def contacts(request):
    return JsonResponse(data={"Contacts": [
        {
            "profile_id": 2,
            "Username": "Test",
            "Last_login": "23.10.2019 22:42"
        },
        {
            "profile_id": 3,
            "Username": "Tester",
            "Last_login": "21.10.2019 22:42"
        }
    ]})


@require_http_methods(['GET'])
def chats(request, username):
    user = get_object_or_404(User, username=username)
    users_chats = Member.objects.filter(user=user).select_related("chat")
    chats_list = []
    for i in users_chats:
        chats_list.append({
            "id": i.chat.id,
            "title": i.chat.title,
            "description": i.chat.description
        })
    return JsonResponse({"chats": chats_list})


@require_http_methods(['POST'])
@csrf_exempt
def create_user(request):
    try:
        User.objects.get(username=request.POST['username'])
        return JsonResponse({"Error": "User with such username already exists"},
                            status=400)
    except User.DoesNotExist:
        pass
    user = User()
    user.username = request.POST['username']
    user.phone_number = request.POST['phone']
    user.first_name = request.POST.get('fname', None)
    user.last_name = request.POST.get('lname', None)
    user.save()
    return JsonResponse({
        'description': 'User with following credentials created',
        'username': user.username,
        'First name': user.first_name,
        'Last name': user.last_name,
    },
        status=200)
