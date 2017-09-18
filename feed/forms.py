from django import forms
from feed.models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = [
            "id"
        ]
        widgets = {
            "author": forms.HiddenInput()
        }
