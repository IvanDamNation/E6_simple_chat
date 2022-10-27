from django import forms
from django.contrib.auth.models import User

from .models import ChatUser


class ChatUserForm(forms.ModelForm):
    class Meta:
        model = ChatUser
        fields = ('avatar', 'chat_username')


class UserFormUpd(forms.ModelForm):
    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
        )
