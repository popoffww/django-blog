from django.urls import path
from .views import home, posts, post_detail, tags, tag_detail

urlpatterns = [
    path('', home, name='home'),
    path('posts/', posts, name='posts'),
    path('post/<str:slug>/', post_detail, name='post_detail'),
    path('tags/', tags, name='tags'),
    path('tag/<str:slug>/', tag_detail, name='tag_detail'),

]