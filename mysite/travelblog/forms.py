from django import forms
from .models import Post, Activity


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'summary', 'content', 'images', 'location', 'city', 'country', 'tags']


class ActivityForm(forms.ModelForm):
    class Meta:
        model = Activity
        fields = ['name', 'description', 'duration', 'cost', 'location', 'suitability', 'city', 'country', 'image']

