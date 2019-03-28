from django.contrib import admin
from .models import Blog, Blogger, Comment

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



