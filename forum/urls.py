from django.urls import path, include
from django.urls.resolvers import URLPattern
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<param_forum_name>', views.forum, name='param_forum_name'),
    path('discussion/<param_discussion>',
         views.discussion_view, name='param_discussion'),
    path('<param_forum_name>/new', views.discussion_new, name='discussion_new'),
    path('discussion/<param_discussion>/edit',
         views.discussion_edit, name='discussion_edit'),
    path('discussion/<param_discussion>/delete',
         views.discussion_delete, name='discussion_delete'),
]
