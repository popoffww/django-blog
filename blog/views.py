from django.shortcuts import render
from django.views.generic import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import Post, Tag

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

class TagDetail(View):
    def get(self, request, slug):
        tag = Tag.objects.get(slug__iexact=slug)
        return render(request, 'blog/tag_detail.html', {'tag': tag})

