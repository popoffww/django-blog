from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView

from .models import Post, Tag
from .forms import PostForm, TagForm

def home(request):
    return render(request, 'blog/home.html')

class PostListView(ListView):
    model = Post
    queryset = Post.objects.filter(draft=False)

class PostDetailView(DetailView):
    model = Post
    slug_field = 'slug'

class PostCreateView(SuccessMessageMixin, CreateView):
    model = Post
    form_class = PostForm
    success_url = reverse_lazy('posts')
    success_message = 'Пост успешно создан'

class PostUpdateView(SuccessMessageMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_update.html'
    success_url = reverse_lazy('posts')
    success_message = 'Пост успешно изменен'

class TagListView(ListView):
    model = Tag
    queryset = Tag.objects.all()

class TagDetailView(DetailView):
    model = Tag
    slug_field = 'slug'

class TagCreateView(SuccessMessageMixin, CreateView):
    model = Tag
    form_class = TagForm
    success_url = reverse_lazy('tags')
    success_message = 'Тэг успешно создан'

class TagUpdateView(SuccessMessageMixin, UpdateView):
    model = Tag
    form_class = TagForm
    template_name = 'blog/tag_update.html'
    success_url = reverse_lazy('tags')
    success_message = 'Тэг успешно изменен'






