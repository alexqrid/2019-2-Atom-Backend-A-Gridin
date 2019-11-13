from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from .models import User


@require_http_methods(['GET', 'POST'])
def profile(request, username):
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        return JsonResponse({"Error": "User does not exists"}, status=404)
    return JsonResponse({
        'username': user.username,
        'First name': user.first_name,
        'Last name': user.last_name
    })


@require_http_methods(['GET', 'POST'])
def contacts(request):
    return JsonResponse(data={"Contacts": [
        {"profile_id": 2,
         "Username": "Test",
         "Last_login": "23.10.2019 22:42"
         },
        {"profile_id": 3,
         "Username": "Tester",
         "Last_login": "21.10.2019 22:42"
         }
    ]})


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
