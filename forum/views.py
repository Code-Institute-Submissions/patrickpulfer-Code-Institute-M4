from django.http import HttpResponseRedirect
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

    context = {
        'forum_data': forum,
        'discussions_data': discussions,
    }
    return render(request, 'forum/forum_view.html', context)


def discussion_view(request, param_discussion):

    if request.method == 'POST' and request.user.is_authenticated:
        comment_form = CommentForm(request.POST)

        if comment_form.is_valid():

            obj = comment_form.save(commit=False)

            discussion = get_object_or_404(Discussion, title=param_discussion)
            obj.discussion = discussion
            obj.poster = request.user
            obj.save()
            return HttpResponseRedirect('/forum/discussion/%s' % discussion.title)

    else:
        discussion = get_object_or_404(Discussion, title=param_discussion)
        comments = Comment.objects.filter(discussion=discussion.id)
        comment_form = CommentForm(instance=request.user.profile)

        context = {
            'discussion': discussion,
            'comments': comments,
            'comment_form': comment_form
        }

        return render(request, 'forum/discussion_view.html', context)
