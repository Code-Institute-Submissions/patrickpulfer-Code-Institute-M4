from django.urls import path, include
from django.urls.resolvers import URLPattern
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<param_forum_name>', views.forum, name='param_forum_name')
]
