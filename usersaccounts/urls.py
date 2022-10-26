from django.urls import path

from .views import personal_page_view

urlpatterns = [
    path('profile/', personal_page_view, name='profile'),
]
