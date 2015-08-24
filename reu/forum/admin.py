from django.contrib import admin
from .models import Forum, Topic, Post

# Register your models here.

class ForumAdmin(admin.ModelAdmin):
    list_display = ('name',)

class PostInline(admin.TabularInline):
    model = Post

class TopicAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_by', 'created_on', 'number_of_posts')
    inlines = [PostInline]

# class PostAdmin(admin.ModelAdmin):
#     list_display = ('body', 'created_by', 'created_on')

admin.site.register(Forum, ForumAdmin)
admin.site.register(Topic, TopicAdmin)
# admin.site.register(Post, PostAdmin)