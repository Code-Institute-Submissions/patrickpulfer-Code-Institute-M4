from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from .models import Profile
from .forms import UserForm, ProfileForm


def profiles(request, username):
    user = get_object_or_404(User, username=username)
    profile = get_object_or_404(Profile, user_id=user.id)
    context = {
        'user_data': user,
        'user_profile': profile,
    }
    return render(request, 'profiles/profile_view.html', context)


def profile_update(request):
    if request.method == 'POST' and request.user.is_authenticated:
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return HttpResponseRedirect('/profiles/%s' % request.user.username)

    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)

    return render(request, 'profiles/profile_update.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })
