from .views import chat_list, chat, hello,create_chat
from django.urls import path

urlpatterns = [
        path('', hello),
        path('list/', chat_list, name='list'),
        path('chat/', chat, name='chat'),
        path('new/', create_chat, name='create')
    ]