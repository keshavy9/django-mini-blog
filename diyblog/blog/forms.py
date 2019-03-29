from django import forms
from .models import Comment, CommentReply

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment',]


class ReplyForm(forms.ModelForm):
    class Meta:
        model = CommentReply
        fields = ['reply',]