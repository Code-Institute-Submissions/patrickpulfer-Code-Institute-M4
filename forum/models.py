from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import NullBooleanField


# Forum Model
class Forum(models.Model):
    name = models.CharField(max_length=20, default="anonymous")
    topic = models.CharField(max_length=300)
    description = models.CharField(max_length=1000, blank=True)
    link = models.CharField(max_length=100, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    visible = models.BooleanField(default=True)
    premium_only = models.BooleanField(default=False, blank=True)

    def __str__(self):
        return str(self.topic)


# Forum Post Model
class Discussion(models.Model):
    forum = models.ForeignKey(Forum, blank=True, on_delete=models.CASCADE)
    poster = models.ForeignKey(User, blank=True, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    date_modified = models.DateTimeField(auto_now=True)
    link = models.CharField(max_length=100, blank=True)
    visible = models.BooleanField(default=True)
    premium_only = models.BooleanField(default=False, blank=True)

    title = models.CharField(max_length=100)
    body = models.CharField(max_length=1000)

    def __str__(self):
        return str(self.forum)


# Comments Model
class Comment(models.Model):
    poster = models.ForeignKey(User, blank=True, on_delete=models.CASCADE)
    discussion = models.ForeignKey(
        Discussion, blank=True, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    date_modified = models.DateTimeField(auto_now=True)
    visible = models.BooleanField(default=True)

    body = models.CharField(max_length=1000)

    def __str__(self):
        return str(self.body)
