from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^forum/$', views.IndexView.as_view(), name='index'),
    url(r'^forum/(?P<forum_name>\w+)/$', views.ForumView.as_view(), name='forum'),
    url(r'^topic/(?P<pk>[0-9]+)/$', views.TopicView.as_view(), name='topic'),
    url(r'^forum/(?P<forum_name>\w+)/newtopic/$', views.new_post, name='new_topic'),
    url(r'^topic/(?P<topic_id>[0-9]+)/newpost/$', views.new_post, name='new_post'),
]