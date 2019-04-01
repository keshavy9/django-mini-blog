from django import forms
from .models import Comment, CommentReply, Blog

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment',]


class ReplyForm(forms.ModelForm):
    class Meta:
        model = CommentReply
        fields = ['reply',]


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog 
        fields = ['title', 'description',]       