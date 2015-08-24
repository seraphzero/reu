from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

# Create your models here.

class Forum(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('forum:forum', kwargs={'forum_name': self.name})

class Topic(models.Model):
    forum = models.ForeignKey(Forum)
    title = models.CharField(max_length=80)
    created_by = models.ForeignKey(User)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('forum:topic', kwargs={'pk': self.id})

    def number_of_posts(self):
        return self.post_set.all().count()

class Post(models.Model):
    topic = models.ForeignKey(Topic)
    created_by = models.ForeignKey(User)
    created_on = models.DateTimeField(auto_now_add=True)
    body = models.TextField()

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return self.body[:80]+'...' if len(self.body) > 80 else self.body