from .models import Post, Comment
from django import forms


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = (
            'title',  
            'event_start', 
            'event_end', 
            'adress', 
            'map_link',
            'featured_image', 
            'category', 
            'description')
        
        labels = {
            'event_start': 'Start date/time',
            'event_end': 'End Time',
            'map_link': 'Map Link (optional)',
            'featured_image': 'Image (optional)',
        }

        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Write a title here'}),
            'description': forms.Textarea(attrs={'placeholder': 'Write a description of your event here'}),
            'event_start': forms.TextInput(attrs={'placeholder': 'xxxx-xx-xx xx:xx:xx'}),
            'event_end': forms.TextInput(attrs={'placeholder': 'xx:xx:xx'}),
            'adress': forms.TextInput(attrs={'placeholder': 'Streetname 1'}),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
        