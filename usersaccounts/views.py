from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404

from .forms import ChatUserForm, UserFormUpd
from .models import ChatUser


@login_required
def user_update_view(request):
    obj = get_object_or_404(User, pk=request.user.pk)
    obj_2 = get_object_or_404(ChatUser, pk=request.user.pk)
    form = UserFormUpd(request.POST or None, instance=obj)
    form_2 = ChatUserForm(request.POST or None, instance=obj_2)

    context = {
        'form': form,
        'form_2': form_2,
        'object': obj
    }
    if all([form.is_valid(), form_2.is_valid()]):
        form.save()
        form_2.save()
        # print('form', form.cleaned_data)
        # print('form_2', form_2.cleaned_data)

        context['message'] = 'Saved.'
    return render(request, 'usersaccounts/user_edit.html', context)


def personal_page_view(request):
    context = {
        'user': request.user
    }
    return render(request, 'usersaccounts/personal_page.html', context)
