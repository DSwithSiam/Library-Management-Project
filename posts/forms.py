from .models import Comment
from django import forms
from .models import Post
      
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'body', ]
   