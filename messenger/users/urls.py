from .views import profile, contacts,create_user
from django.urls import path


urlpatterns = [
        path('profile/<str:username>', profile, name='profile'),
        path('contacts/', contacts, name='contacts'),
        path('new/', create_user, name='create')
    ]