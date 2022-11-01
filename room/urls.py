from django.urls import path

from . import views

urlpatterns = [
    path('', views.rooms, name='rooms'),
    path('create_room/', views.room_create, name='create_room'),
    path('<slug:slug>', views.room, name='room'),
]
