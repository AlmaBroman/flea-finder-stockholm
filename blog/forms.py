from .models import Post, Comment
from django import forms


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = (
            'title',  
            'start_date', 
            'start_time',
            'end_time', 
            'adress', 
            'map_link',
            'featured_image', 
            'category', 
            'description')
        
        labels = {
            'date': 'Date', 
            'start_time': 'Start Time', 
            'end_time': 'End Time', 
            'map_link': 'Map Link (optional)', 
            'featured_image': 'Image (optional)', 
        }

        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Write a title here'}),
            'description': forms.Textarea(attrs={'placeholder': 'Write a description of your event here'}),
            'start_date': forms.DateInput(attrs={'type': 'date', 'placeholder': 'yyyy-mm-dd', 'class': 'form-control'}), 
            'start_time': forms.TimeInput(attrs={'type': 'time'}),
            'end_time': forms.TimeInput(attrs={'type': 'time'}),
            'adress': forms.TextInput(attrs={'placeholder': 'Streetname 1'}),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
        