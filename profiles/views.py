from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from .models import Profile
from django.contrib.auth.models import User


def profiles(request, username):
    profile = get_object_or_404(User, username=username)
    context = {
        'profile': profile,
    }
    return render(request, 'profiles/index.html', context)
