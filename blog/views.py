from django.shortcuts import render
from django.views import generic
from .models import Post


class PostList (generic.ListView):
    model = Post
    queryset = Post.objects.order_by('event_start')
    template_name = 'index.html'
    paginate_by = 6