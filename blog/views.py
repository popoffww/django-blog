from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.db.models import Q

from .models import Post, Tag
from .forms import PostForm, TagForm


class HomePageView(TemplateView):
    template_name = 'blog/home.html'


class PostListView(ListView):
    model = Post
    queryset = Post.objects.filter(draft=False)
    paginate_by = 2

    def get_queryset(self):
        query = self.request.GET.get('q', '')
        post_list = Post.objects.filter(
            Q(title__icontains=query)|Q(body__icontains=query)
        )
        return post_list


class PostDetailView(DetailView):
    model = Post
    slug_field = 'slug'


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    success_url = reverse_lazy('posts')
    raise_exception = True

class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_update.html'
    success_url = reverse_lazy('posts')
    raise_exception = True

class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('posts')
    raise_exception = True

    # def get(self, request, *args, **kwargs):
    #     return self.post(request, *args, **kwargs)


class TagListView(ListView):
    model = Tag
    queryset = Tag.objects.all()


class TagDetailView(DetailView):
    model = Tag
    slug_field = 'slug'


class TagCreateView(LoginRequiredMixin, CreateView):
    model = Tag
    form_class = TagForm
    success_url = reverse_lazy('tags')
    raise_exception = True

class TagUpdateView(LoginRequiredMixin, UpdateView):
    model = Tag
    form_class = TagForm
    template_name = 'blog/tag_update.html'
    success_url = reverse_lazy('tags')
    raise_exception = True

class TagDeleteView(LoginRequiredMixin, DeleteView):
    model = Tag
    success_url = reverse_lazy('tags')
    raise_exception = True

    # def get(self, request, *args, **kwargs):
    #     return self.post(request, *args, **kwargs)
