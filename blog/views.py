from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Post, Tag
from .forms import PostForm, TagForm

class HomePageView(TemplateView):
    template_name = 'blog/home.html'

class PostListView(ListView):
    model = Post
    queryset = Post.objects.filter(draft=False)

class PostDetailView(DetailView):
    model = Post
    slug_field = 'slug'

class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    success_url = reverse_lazy('posts')

class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_update.html'
    success_url = reverse_lazy('posts')

class PostDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy('posts')

    # def get(self, request, *args, **kwargs):
    #     return self.post(request, *args, **kwargs)

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

class TagUpdateView(UpdateView):
    model = Tag
    form_class = TagForm
    template_name = 'blog/tag_update.html'
    success_url = reverse_lazy('tags')

class TagDeleteView(DeleteView):
    model = Tag
    success_url = reverse_lazy('tags')

    # def get(self, request, *args, **kwargs):
    #     return self.post(request, *args, **kwargs)






