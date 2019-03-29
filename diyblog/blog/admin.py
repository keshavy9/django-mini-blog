from django.contrib import admin
from .models import Blog, Blogger, Comment, CommentReply, Like

# Register your models here.


@admin.register(Blog)
class Blog(admin.ModelAdmin):
    pass

@admin.register(Blogger)
class Blogger(admin.ModelAdmin):
    pass

@admin.register(Comment)
class Comment(admin.ModelAdmin):
    pass

@admin.register(CommentReply)
class CommentReply(admin.ModelAdmin):
    pass

@admin.register(Like)
class Like(admin.ModelAdmin):
    pass    
