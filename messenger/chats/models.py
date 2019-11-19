from django.db import models
from django.urls import reverse
from users.models import User
import datetime


class Chat(models.Model):
    is_group = models.BooleanField(verbose_name='Is group chat?', default=False)
    title = models.CharField(verbose_name="Chat's Title", max_length=128)
    description = models.CharField(verbose_name="Chat's description", max_length=512,
                                   default='Chat for debates')
    icon = models.ImageField(upload_to='images/', blank=True, null=True,)

    class Meta:
        """class for additional info"""
        verbose_name = "Chat"
        verbose_name_plural = "Chats"
        ordering = ["id"]

    def get_absolute_url(self):
        reverse('chat', kwargs={'chat_id': self.id})

    def __str__(self):
        return self.title


class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             verbose_name="Message sender")
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE,
                             verbose_name='The source chat\'s id')
    content = models.TextField(blank=False, verbose_name='Message\'s content')

    created_at = models.DateTimeField(default=datetime.datetime.now(), verbose_name= "Message creation time")

    class Meta:
        """class for additional info"""
        verbose_name = "Message"
        verbose_name_plural = "Messages"
        ordering = ["chat_id"]


class Attachment(models.Model):
    mesg = models.ForeignKey(Message, verbose_name='Message\'s id where this attachment had been sent',
                             on_delete=models.CASCADE)
    attachment_type = models.CharField(max_length=64, blank=False)

    path = models.TextField(blank=False,
                            verbose_name='URL or path to the location of the attachment')

    class Meta:
        """class for additional info"""
        verbose_name = "Attachment"
        verbose_name_plural = "Attachments"
        ordering = ["mesg_id"]


class Member(models.Model):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)

    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)

    last_msg = models.ForeignKey(Message, verbose_name="Last read message",
                                 blank=True, null=True, on_delete=models.CASCADE, default=None)

    new_msg = models.BooleanField(blank=True, null=True,
                                  verbose_name='Is there new message in the chat?', default=False)
