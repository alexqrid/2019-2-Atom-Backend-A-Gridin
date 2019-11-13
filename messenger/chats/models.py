from django.db import models
from django.urls import reverse


class Chat(models.Model):
    is_group = models.BooleanField(verbose_name='Is group chat?', default=False)
    title = models.CharField(verbose_name="Chat's Title", max_length=128)
    description = models.CharField(verbose_name="Chat's description", max_length=512,
                                   default='Chat for debates')

    class Meta:
        """class for additional info"""
        verbose_name = "Chat"
        verbose_name_plural = "Chats"
        ordering = ["id"]

    def get_absolute_url(self):
        reverse('Chat', kwargs={'chat_id': self.id})

    def __str__(self):
        return self.title


class Message(models.Model):
    chat_id = models.ForeignKey(Chat, on_delete=models.CASCADE,
                                verbose_name='The source chat\'s id')
    content = models.TextField(blank=False,verbose_name='Message\'s content')

    class Meta:
        """class for additional info"""
        verbose_name = "Message"
        verbose_name_plural = "Messages"
        ordering = ["chat_id"]


class Attachment(models.Model):
    mesg_id = models.ForeignKey(Message, verbose_name='Message\'s id where this attachment had been sent',
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
    user_id = models.ForeignKey('users.User', on_delete=models.CASCADE)
    chat_id = models.ForeignKey(Chat, on_delete=models.CASCADE)
    last_msg_id = models.ForeignKey(Message, blank=True,null=True, on_delete=models.CASCADE)
    new_mesg = models.BooleanField(blank=True, null=True,
                                   verbose_name='Is there new message in the chat?', default=False)
