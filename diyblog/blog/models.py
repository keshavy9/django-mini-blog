from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


# Create your models here.

class Blog(models.Model):

    title = models.CharField(max_length=200, help_text="Enter a title for the blog post", null = True)
    blogger = models.ForeignKey('Blogger', on_delete = models.SET_NULL, null = True)
    date = models.DateTimeField(auto_now=True)
    description = models.TextField(max_length=1000, help_text="Add the blog content", null=True)
   


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog-detail', args = [str(self.id)])    


class Blogger(models.Model):

    name = models.CharField(max_length=50, help_text="Blogger's name", null=True)
    bio = models.TextField(max_length=200, help_text="Description about the blogger", null=True)
    user = models.ForeignKey(User, null=True, on_delete= models.SET_NULL)

    def __str__(self):
        return self.name

    
    def get_absolute_url(self):
        return reverse('blogger-detail', args = [str(self.id)])        

class Comment(models.Model):

    comment = models.CharField(max_length=100, null=True)
    commenter = models.ForeignKey(User,  on_delete = models.SET_NULL, null = True)
    blog = models.ForeignKey(Blog, on_delete = models.SET_NULL, related_name='comments', null = True)
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment


class CommentReply(models.Model):

    reply = models.CharField(max_length=100, null = True)  
    comment = models.ForeignKey(Comment, on_delete = models.SET_NULL, related_name='replies',null = True)    
    replier = models.ForeignKey(User, on_delete = models.SET_NULL, null = True)
    added_at = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return self.reply


class Like(models.Model):

    liked_by = models.ForeignKey(User, on_delete = models.SET_NULL, null = True, related_name='+')
    post = models.ForeignKey(Blog, on_delete = models.SET_NULL, null = True, related_name='likes' )
  