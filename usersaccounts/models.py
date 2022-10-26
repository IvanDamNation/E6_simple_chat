from django.contrib.auth.models import User
from django.db import models


class ChatUser(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    chat_username = models.CharField(max_length=32, blank=True, verbose_name='chat_username')
    avatar = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='avatar', blank=True)

    def __str__(self):
        return '{}'.format(self.user.username)

    class Meta:
        verbose_name = 'Chat user'
        verbose_name_plural = 'Users of the chat'
