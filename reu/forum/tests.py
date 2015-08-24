from django.test import TestCase
from django.contrib.auth.models import User
from .models import Forum, Topic, Post

# Create your tests here.

class ForumViewTests(TestCase):
    def test_forum_view_with_no_topics(self):
        """
        If no topics exist, an appropriate message should be displayed.
        """
        forum = Forum.objects.create(name='Test')
        response = self.client.get(forum.get_absolute_url())
        self.assertEquals(response.status_code, 200)
        self.assertContains(response, 'There are no topics to show here.')
        self.assertQuerysetEqual(response.context['topic_list'], [])

    def test_forum_view_with_topics(self):
        """
        Forums with topic(s) should have the topics be displayed.
        """
        user = User.objects.create(username='admin', password='hunter2')
        forum = Forum.objects.create(name='Test')
        topic1 = Topic.objects.create(forum=forum, title='Topic 1', created_by=user)
        topic2 = Topic.objects.create(forum=forum, title='Topic 2', created_by=user)
        response = self.client.get(forum.get_absolute_url())
        self.assertEquals(response.status_code, 200)
        self.assertQuerysetEqual(response.context['topic_list'], ['<Topic: Topic 2>', '<Topic: Topic 1>'])

class TopicViewTest(TestCase):
    def test_topic_view_with_no_posts(self):
        """
        Topic should not exist without any posts.
        """
        user = User.objects.create(username='admin', password='hunter2')
        forum = Forum.objects.create(name='Test')
        topic = Topic.objects.create(forum=forum, title='Topic', created_by=user)
        response = self.client.get(topic.get_absolute_url())
        self.assertEquals(response.status_code, 404)
        self.assertEquals(topic.number_of_posts == 0, False)

    def test_topic_view_with_posts(self):
        """
        Topic should have posts be displayed in chronological order.
        """
        user = User.objects.create(username='admin', password='hunter2')
        forum = Forum.objects.create(name='Test')
        topic = Topic.objects.create(forum=forum, title='Topic', created_by=user)
        post1 = Post.objects.create(topic=topic, created_by=user, body='First post.')
        post2 = Post.objects.create(topic=topic, created_by=user, body='Second post.')
        response = self.client.get(topic.get_absolute_url())
        self.assertEquals(response.status_code, 200)
        self.assertEquals(topic.number_of_posts != 0, True)
        self.assertQuerysetEqual(topic.post_set.all(), ['<Post: First post.>', '<Post: Second post.>'])
