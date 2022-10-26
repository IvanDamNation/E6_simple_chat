from django.shortcuts import render
from .forms import ChatUserForm


def personal_page_view(request):
    context = {
        'user': request.user
    }
    return render(request, 'usersaccounts/personal_page.html', context)
