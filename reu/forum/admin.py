from django.contrib import admin
from .models import Forum, Thread, Post

# Register your models here.

class ForumAdmin(admin.ModelAdmin):
    list_display = ('name',)

class PostInline(admin.TabularInline):
    model = Post

class ThreadAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_by', 'created_on')
    inlines = [PostInline]

# class PostAdmin(admin.ModelAdmin):
#     list_display = ('body', 'created_by', 'created_on')

admin.site.register(Forum, ForumAdmin)
admin.site.register(Thread, ThreadAdmin)
# admin.site.register(Post, PostAdmin)