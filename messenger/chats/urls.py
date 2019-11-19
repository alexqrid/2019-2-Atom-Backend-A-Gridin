from .views import chat_list, chat, hello, create_chat, new_chat, send_message, read_message
from django.urls import path

urlpatterns = [
    path('', hello, name='index'),
    path('list/', chat_list, name='list'),
    path('chat/<int:chat_id>/', chat, name='chat'),
    path('new/', create_chat, name='create'),
    path('newch/', new_chat, name='new chat'),
    path('chat/<int:chat_id>/new_message', send_message, name='create message'),
    path('chat/<int:chat_id>/<str:username>', read_message, name='read message')
]
