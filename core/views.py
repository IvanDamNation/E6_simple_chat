from django.contrib.auth import login
from django.shortcuts import render, redirect

from .forms import SignUpForm
from usersaccounts.forms import ChatUserForm


def frontpage(request):
    return render(request, 'core/frontpage.html')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        additional_form = ChatUserForm(request.POST)

        if form.is_valid() and additional_form.is_valid():
            user = form.save()
            chat_user = additional_form.save(commit=False)
            chat_user.user = user

            chat_user.save()

            login(request, user)

            return redirect('frontpage')

    else:
        form = SignUpForm()
        additional_form = ChatUserForm()

    return render(request, 'core/signup.html', {'form': form, 'additional_form': additional_form})
