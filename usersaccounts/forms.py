from django import forms

from .models import ChatUser


class ChatUserForm(forms.ModelForm):
    class Meta:
        model = ChatUser
        fields = ('avatar', 'chat_username')
