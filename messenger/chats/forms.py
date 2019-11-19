from django import forms
from .models import Message, Member
from users.models import User
from .utils import user_exists


class ChatCreateForm(forms.Form):
    sender = forms.CharField(max_length=64)#validators=[user_exists], max_length=64)
    recipient = forms.CharField(max_length=64)#validators=[user_exists], max_length=64)
    title = forms.CharField(max_length=128)
    description = forms.CharField(required=False)
    message = forms.CharField(widget=forms.Textarea(
                                    attrs={
                                        "placeholder": "Your message"
                                }
    ))

    def clean(self):
        cleaned_data = self.cleaned_data
        users = [cleaned_data.get('sender'), cleaned_data.get('recipient')]
        user = User.objects.filter(username__iexact=users[0])
        if len(user) != 1:
            self.add_error('sender', "User does not exist")
        user = User.objects.filter(username__iexact=users[1])
        if len(user) != 1:
            self.add_error('recipient', "User does not exist")
        return cleaned_data


class CreateMessageForm(forms.ModelForm):

    class Meta:
        model = Message
        fields = ['content', "user"]


class AttachmentForm(forms.Form):
    message
