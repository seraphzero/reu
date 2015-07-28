from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Forum(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Thread(models.Model):
    forum = models.ForeignKey(Forum)
    title = models.CharField(max_length=80)
    created_by = models.ForeignKey(User)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Post(models.Model):
    thread = models.ForeignKey(Thread)
    created_by = models.ForeignKey(User)
    created_on = models.DateTimeField(auto_now_add=True)
    body = models.TextField()

    def __str__(self):
        return self.body[:80]+'...' if len(self.body) > 80 else self.body