from .views import profile, contacts, create_user, chats
from django.urls import path


urlpatterns = [
        path('<str:username>', profile, name='profile'),
        path('contacts/', contacts, name='contacts'),
        path('new/', create_user, name='create'),
        path('<str:username>/chats', chats, name="user_chat_list")
    ]