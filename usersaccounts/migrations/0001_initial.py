# Generated by Django 4.1.2 on 2022-10-23 18:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ChatUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chat_username', models.CharField(blank=True, max_length=32, verbose_name='chat_username')),
                ('avatar', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/', verbose_name='avatar')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Chat user',
                'verbose_name_plural': 'Users of the chat',
            },
        ),
    ]
