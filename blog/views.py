from django.shortcuts import render
from .models import Post

def home(request):
    return render(request, 'blog/home.html')

def posts_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/posts.html', {'posts': posts})

def tags_list(request):
    tags = Post.objects.all()
    return render(request, 'blog/tags.html', {'tags': tags})

