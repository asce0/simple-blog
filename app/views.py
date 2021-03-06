from django.shortcuts import render
from django.views import generic
from .models import Post

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'app/home.html'

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'app/postdetail.html'
