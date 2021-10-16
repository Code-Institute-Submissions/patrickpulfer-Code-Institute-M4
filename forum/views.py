from django.shortcuts import render, get_object_or_404
from .models import Forum, Discussion, Comment
from django.contrib.auth.models import User
from .forms import CommentForm


def home(request):
    forums = Forum.objects.all()
    return render(request, 'forum/index.html', {'forums': forums})


def forum(request, param_forum_name):

    forum = get_object_or_404(Forum, forum_name=param_forum_name)
    discussions = Discussion.objects.filter(forum=forum.id)

    #comments = Comment.objects.filter(discussions)
    # print(list(discussions))
    #comments = get_object_or_404(Discussion, id=discussions)

#comments = Comment.objects.filter(discussion=discussions)

# poster = Discussion.objects.filter(poster=User.id)

# print(comments)


# print("Forum Topic: ")
    # print(list(discussions))
    # int("Model:")
    # print(list(Forum.forum_name))
    # print(Forum)
    # discussions = Discussion.objects.filter(forum=forum)

    context = {
        'forum_data': forum,
        'discussions_data': discussions,
        #    'comments_data': comments
    }
    return render(request, 'forum/forum_view.html', context)


def discussion_view(request, param_discussion):
    discussion = get_object_or_404(Discussion, title=param_discussion)
    comments = Comment.objects.filter(discussion=discussion.id)

    comment_form = CommentForm(instance=request.user.profile)

    context = {
        'discussion': discussion,
        'comments': comments,
        'comment_form': comment_form
    }
    return render(request, 'forum/discussion_view.html', context)
