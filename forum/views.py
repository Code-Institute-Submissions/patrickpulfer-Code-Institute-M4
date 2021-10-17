from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .models import Forum, Discussion, Comment
from profiles.models import Profile
from django.contrib.auth.models import User
from .forms import CommentForm, ForumNewTopic, Discussion_Edit_Form


def home(request):
    if request.user.is_authenticated:
        forums = Forum.objects.all()
        user = get_object_or_404(User, username=request.user)
        profile = get_object_or_404(Profile, user_id=user.id)
        context = {
            'user': user,
            'profile': profile,
            'forums': forums,
        }
    else:
        forums = Forum.objects.all()
        context = {'forums': forums}
    return render(request, 'forum/index.html', context)


def forum(request, param_forum_name):
    if request.user.is_authenticated:
        user = get_object_or_404(User, username=request.user)
        profile = get_object_or_404(Profile, user_id=user.id)
    else:
        profile = ''

    forum = get_object_or_404(Forum, forum_name=param_forum_name)
    discussions = Discussion.objects.filter(forum=forum.id)
    context = {
        'forum_data': forum,
        'discussions_data': discussions,
        'profile': profile,
    }
    return render(request, 'forum/forum_view.html', context)


def forum_new(request, param_forum_name):
    forum = get_object_or_404(Forum, forum_name=param_forum_name)
    if request.method == 'POST' and request.user.is_authenticated:
        discussion_form = ForumNewTopic(request.POST, request.FILES,)
        if discussion_form.is_valid():
            obj = discussion_form.save(commit=False)
            obj.forum = forum
            obj.poster = request.user
            obj.visible = True
            obj.save()
            return HttpResponseRedirect('/forum/discussion/%s' % discussion_form['title'].value())

    else:
        discussion_form = ForumNewTopic(instance=request.user.profile)
        context = {
            'forum_data': forum,
            'discussion_form': discussion_form,
        }
        return render(request, 'forum/forum_new.html', context)


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
        if request.user.is_authenticated:
            comment_form = CommentForm(instance=request.user.profile)
        else:
            comment_form = ''
        context = {
            'discussion': discussion,
            'comments': comments,
            'comment_form': comment_form
        }
        return render(request, 'forum/discussion_view.html', context)


def discussion_edit(request, param_discussion):
    discussion = get_object_or_404(Discussion, title=param_discussion)

    if request.method == 'POST' and request.user.is_authenticated:
        discussion_form = Discussion_Edit_Form(request.POST, request.FILES)
        if discussion_form.is_valid():
            obj = discussion_form.save(commit=False)
            obj.forum = discussion.forum
            obj.poster = obj.poster = request.user
            obj.save()
            return HttpResponseRedirect('/forum/discussion/%s' % discussion_form['title'].value())

    else:
        discussion_form = Discussion_Edit_Form(instance=discussion)
        context = {
            'discussion': discussion,
            'discussion_form': discussion_form,
        }
        return render(request, 'forum/discussion_edit.html', context)
