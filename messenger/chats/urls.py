from .views import chat_list, profile, contacts, chat, hello
from django.urls import path

urlpatterns = [
        path('', hello),
        path('list/', chat_list, name='list'),
        path('profile/<int:id>', profile, name='profile'),
        path('contacts', contacts, name='contacts'),
        path('chat', chat, name='chat')
    ]