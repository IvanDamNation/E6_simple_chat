from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import UpdateView

from .forms import ChatUserForm, UserFormUpd


class ChatUserUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'usersaccounts/user_edit.html'
    form_class = UserFormUpd
    success_url = '/'

    def get_object(self, **kwargs):
        return self.request.user


def personal_page_view(request):
    context = {
        'user': request.user
    }
    return render(request, 'usersaccounts/personal_page.html', context)
