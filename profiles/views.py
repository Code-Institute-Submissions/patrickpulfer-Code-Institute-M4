from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from .models import Profile


def profiles(request, username):
    user = get_object_or_404(User, username=username)
    profile = get_object_or_404(Profile, user_id=user.id)
    context = {
        'user_data': user,
        'user_profile': profile,
    }
    return render(request, 'profiles/index.html', context)
