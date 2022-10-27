from django.urls import path

from .views import personal_page_view, ChatUserUpdateView

urlpatterns = [
    path('profile/', personal_page_view, name='profile'),
    path('edit/', ChatUserUpdateView.as_view(), name='edit_profile'),
]
