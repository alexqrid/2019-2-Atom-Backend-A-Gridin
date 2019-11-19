from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse


class User(AbstractUser):
    username = models.CharField(unique=True, max_length=64)
    first_name = models.CharField(blank=True, max_length=64)
    last_name = models.CharField(blank=True, max_length=64)
    phone_number = models.CharField(blank=True, max_length=20)
    registration_date = models.DateTimeField(blank=False,
                                             verbose_name='User\'s registration date',
                                             auto_now_add=True)

    class Meta:
        """class for additional info"""
        verbose_name = "User"
        verbose_name_plural = "Users"
        ordering = ["id"]

    def get_absolute_url(self):
        reverse('users', kwargs={'chat_id': self.id})

    def __str__(self):
        return self.username
