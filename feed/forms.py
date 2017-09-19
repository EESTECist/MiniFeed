from django import forms
from django.forms import TextInput, Select

from feed.models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = [
            "id"
        ]
        widgets = {
            "author": forms.HiddenInput(),
            "body": TextInput(attrs={"class": "form-control", "placeholder": "What are you up to?"}),
            "category": Select(attrs={"class": "form-control"})
        }
