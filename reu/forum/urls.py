from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^forum/$', views.index, name='index'),
    url(r'^forum/(?P<forum_name>\w+)/$', views.forum, name='forum'),
    url(r'^topic/(?P<topic_id>[0-9]+)/$', views.topic, name='topic'),
]