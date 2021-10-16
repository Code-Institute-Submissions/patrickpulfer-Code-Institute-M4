from django.shortcuts import render, get_object_or_404
from .models import Forum, Discussion, Comment


def home(request):
    forums = Forum.objects.all()
    return render(request, 'forum/index.html', {'forums': forums})


def forum(request, forum_name):
    forum = Forum.objects.filter(forum_name=forum_name)
    discussions = Discussion.objects.filter(forum=forum)
    comments = Comment.objects.filter(discussion=discussions)

    context = {
        'forum_data': forum,
        'discussions_data': discussions,
        'comments_data': comments
    }
    return render(request, 'forum/forum_view.html', context)
