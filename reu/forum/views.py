from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Forum, Topic, Post

# Create your views here.

def index(request):
    forum_list = Forum.objects.order_by('name')
    context = {'forum_list': forum_list}
    return render(request, 'forum/index.html', context)

def forum(request, forum_name):
    forum = get_object_or_404(Forum, name=forum_name)
    topics = forum.topic_set.all()
    context = {'forum': forum, 'topics': topics}
    return render(request, 'forum/forum.html', context)

def topic(request, topic_id):
    topic = get_object_or_404(Topic, id=topic_id)
    context = {'topic': topic}
    return render(request, 'forum/topic.html', context)