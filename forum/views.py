from django.shortcuts import render, get_object_or_404
from .models import Forum, Discussion, Comment
from django.contrib.auth.models import User


def home(request):
    forums = Forum.objects.all()
    return render(request, 'forum/index.html', {'forums': forums})


def forum(request, param_forum_name):
    print("Forum Name: " + param_forum_name)
    forum = get_object_or_404(Forum, forum_name=param_forum_name)
    discussions = Discussion.objects.filter(forum=forum.id)
  #  poster = Discussion.objects.filter(poster=User.id)

    #print("Forum Topic: ")
    # print(list(forum))
    # int("Model:")
    # print(list(Forum.forum_name))
    # print(Forum)
    #discussions = Discussion.objects.filter(forum=forum)
   # comments = Comment.objects.filter(discussion=discussions)

    context = {
        'forum_data': forum,
        'discussions_data': discussions,
        # 'poster_data': poster,
        #  'comments_data': comments
    }
    return render(request, 'forum/forum_view.html', context)
