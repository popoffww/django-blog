from django.shortcuts import render
from .models import Post, Tag

def home(request):
    posts = Post.objects.filter(draft=False)
    return render(request, 'blog/home.html', {'posts': posts})

def posts(request):
    posts = Post.objects.filter(draft=False)
    return render(request, 'blog/posts.html', {'posts': posts})

def post_detail(request, slug):
    post = Post.objects.get(slug__iexact=slug)
    return render(request, 'blog/post_detail.html', {'post': post})

def tags(request):
    tags = Tag.objects.all()
    return render(request, 'blog/tags.html', {'tags': tags})

def tag_detail(request, slug):
    tag = Tag.objects.get(slug__iexact=slug)
    return render(request, 'blog/tag_detail.html', {'tag': tag})

