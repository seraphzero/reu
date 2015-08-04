from django import forms
from .models import Topic, Post

class NewPostForm(forms.ModelForm):
    title = forms.CharField(max_length=80, label='Topic Title', widget=forms.TextInput(attrs={'style': 'width:600px'}))

    class Meta:
        model = Post
        fields = ['body']
        widgets = {
            'body': forms.Textarea(attrs={'style': 'width:600px', 'rows': 20}),
        }

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        self.forum = kwargs.pop('forum', None)
        self.topic = kwargs.pop('topic', None)
        super().__init__(*args, **kwargs)

        if self.topic:
            self.fields['title'].required = False

    def save(self):
        if self.forum:
            self.topic = Topic(forum=self.forum, title=self.cleaned_data['title'], created_by=self.user)
            self.topic.save()
        post = Post(topic=self.topic, created_by=self.user, body=self.cleaned_data['body'])
        post.save()

        return self.topic
