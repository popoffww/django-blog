from django.urls import path
from .views import *

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('master/', MasterPageView.as_view(), name='master'),
    path('posts/', PostListView.as_view(), name='posts'),
    path('post/create', PostCreateView.as_view(), name='post_create'),
    path('post/<str:slug>/update/', PostUpdateView.as_view(), name='post_update'),
    path('post/<str:slug>/remove/', PostDeleteView.as_view(), name='post_remove'),
    path('post/<str:slug>/', PostDetailView.as_view(), name='post_detail'),
    path('tags/', TagListView.as_view(), name='tags'),
    path('tag/create', TagCreateView.as_view(), name='tag_create'),
    path('tag/<str:slug>/update/', TagUpdateView.as_view(), name='tag_update'),
    path('tag/<str:slug>/remove/', TagDeleteView.as_view(), name='tag_remove'),
    path('tag/<str:slug>/', TagDetailView.as_view(), name='tag_detail'),
]
