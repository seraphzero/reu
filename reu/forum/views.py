from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.views import generic
from .models import Forum, Topic, Post
from .forms import NewPostForm

# Create your views here.

class IndexView(generic.ListView):
    template_name = 'forum/index.html'

    def get_queryset(self):
        return Forum.objects.order_by('name')

class ForumView(generic.ListView):
    model = Topic
    template_name = 'forum/forum.html'
    # context_object_name = 'topics'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['forum'] = get_object_or_404(Forum, name=self.kwargs['forum_name'])
        return context

    def get_queryset(self):
        self.forum = get_object_or_404(Forum, name=self.kwargs['forum_name'])
        return Topic.objects.filter(forum=self.forum)

class TopicView(generic.DetailView):
    model = Post
    template_name = 'forum/topic.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['topic'] = get_object_or_404(Topic, id=self.kwargs['pk'])
        return context

# class TopicCreate(generic.edit.CreateView):
#     model = Topic
#     fields = ['title']
#     template_name = 'forum/new_topic.html'
#     # form_class = NewTopicForm

#     def form_valid(self, form):
#         user = User.objects.get(username='admin')
#         form.instance.created_by = user
#         return super().form_valid(form)

# def index(request):
#     forum_list = Forum.objects.order_by('name')
#     context = {'forum_list': forum_list}
#     return render(request, 'forum/index.html', context)

# def forum(request, forum_name):
#     forum = get_object_or_404(Forum, name=forum_name)
#     topics = forum.topic_set.all()
#     context = {'forum': forum, 'topics': topics}
#     return render(request, 'forum/forum.html', context)

# def topic(request, topic_id):
#     topic = get_object_or_404(Topic, id=topic_id)
#     context = {'topic': topic}
#     return render(request, 'forum/topic.html', context)

def new_post(request, forum_name=None, topic_id=None):
    user = User.objects.get(username='admin')
    kwargs = {'user': user}
    context = {}

    if forum_name:
        forum = get_object_or_404(Forum, name=forum_name)
        kwargs['forum'] = forum
        context['forum'] = forum

    if topic_id:
        topic = get_object_or_404(Topic, id=topic_id)
        kwargs['topic'] = topic
        context['topic'] = topic

    if request.method == 'POST':
        form = NewPostForm(request.POST, **kwargs)

        if form.is_valid():
            topic = form.save()
            return HttpResponseRedirect(topic.get_absolute_url())

    form = NewPostForm()
    context['form'] = form

    return render(request, 'forum/new_post.html', context)