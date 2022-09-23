from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'post_type',
            'post_name',
            'post_value',
            'post_category',
            'post_author',
        ]
        labels = {
            'post_type': 'Type of post',
            'post_name': 'Title',
            'post_value': 'Enter the text',
            'post_category': 'Choose the category',
            'post_author': 'Author',
        }
