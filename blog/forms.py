from .models import Post, Comment, Category
from django import forms
from django_summernote.widgets import SummernoteWidget

choices = Category.objects.all().values_list('name','name')

choice_list = []

for item in choices:
    choice_list.append(item)


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
            'image_alt',
            'category', 
            'description')
        
        labels = {
            'date': 'Date', 
            'start_time': 'Start Time', 
            'end_time': 'End Time', 
            'map_link': 'Map Link (optional)', 
            'featured_image': 'Image (optional)',
            'image_alt': 'Image Description (optional)',
        }

        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Write a title here'}),
            'description': SummernoteWidget(attrs={'placeholder': 'Write a description of your event here...'}),
            'start_date': forms.DateInput(attrs={'type': 'date', 'placeholder': 'yyyy-mm-dd', 'class': 'form-control'}), 
            'start_time': forms.TimeInput(attrs={'type': 'time'}),
            'category': forms.Select(choices=choice_list),
            'end_time': forms.TimeInput(attrs={'type': 'time'}),
            'adress': forms.TextInput(attrs={'placeholder': 'Streetname 1'}),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
        