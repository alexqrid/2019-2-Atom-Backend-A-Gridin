from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.template.defaultfilters import register
from django.http import JsonResponse
from django.urls import get_resolver


@require_http_methods(['GET'])
def chat_list(request):
    return JsonResponse({
                         "chats_count": 2,
                         "chats": [{
                                     "id":121312,
                                     "Members_id":[1,2,43,4],
                                     "admins_id":[2],
                                      },
                                    {
                                      "id": 2,
                                      "Members_id": [1, 3, 2, 9],
                                      "admins_id": [2]
                                    }]
    })


@require_http_methods(['GET'])
def profile(request, id=0):
    return JsonResponse({"profile_id": id,
                         "Username": "Test",
                         "Last_login": "23.10.2019 22:42",
                         "chats_id": [1,2]})


@require_http_methods(['GET'])
def contacts(request):
    return JsonResponse({"Contacts":[
                                    {"profile_id": 2,
                                     "Username":"Test",
                                     "Last_login": "23.10.2019 22:42"
                                     },
                                    {"profile_id": 3,
                                     "Username": "Tester",
                                     "Last_login": "21.10.2019 22:42"
                                     }
                                    ]})


@require_http_methods(['GET'])
def chat(request):
    return JsonResponse({
                            "last_messages_count": 10,
                            "last_message_id": 103,
                            "opponent_id": 2
                        })


@require_http_methods(["GET"])
def hello(request, name="Stranger"):
    return render(request, 'Hello.html', {'name': name,'links': get_resolver().reverse_dict.keys()})