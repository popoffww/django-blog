from django.urls import path
from .views import home, posts, post_detail, tags

urlpatterns = [
    path('', home, name='home'),
    path('posts/', posts, name='posts'),
    path('post/<str:slug>/', post_detail, name='post_detail'),
    path('tags/', tags, name='tags'),
]