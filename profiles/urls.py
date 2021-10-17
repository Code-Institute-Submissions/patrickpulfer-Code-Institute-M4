from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

urlpatterns = [
    #path('', views.profiles, name='profiles'),
    path('<username>', views.profiles, name='profiles'),
    path('update/', views.profile_update, name='profile_update'),
    path('delete/', views.profile_delete, name='profile_delete'),

]
