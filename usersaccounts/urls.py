from django.urls import path

from .views import personal_page_view, user_update_view

urlpatterns = [
    path('profile/', personal_page_view, name='profile'),
    path('edit/', user_update_view, name='edit_profile'),
]
