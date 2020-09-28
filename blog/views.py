from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView

from .models import Post, Tag
from .forms import TagForm

class HomeListView(ListView):
    model = Post
    queryset = Post.objects.filter(draft=False)
    template_name = 'blog/home.html'

class PostListView(ListView):
    model = Post
    queryset = Post.objects.filter(draft=False)

class PostDetailView(DetailView):
    model = Post
    slug_field = 'slug'

class TagListView(ListView):
    model = Tag
    queryset = Tag.objects.all()

class TagDetailView(DetailView):
    model = Tag
    slug_field = 'slug'

class TagCreateView(CreateView):
    model = Tag
    form_class = TagForm
    success_url = reverse_lazy('tags')






