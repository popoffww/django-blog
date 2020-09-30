from django.urls import path
from .views import *

urlpatterns = [
    path('', HomeListView.as_view(), name='home'),
    path('posts/', PostListView.as_view(), name='posts'),
    path('post/<str:slug>/', PostDetailView.as_view(), name='post_detail'),
    path('post/create', PostCreateView.as_view(), name='post_create'),
    path('tags/', TagListView.as_view(), name='tags'),
    path('tag/create', TagCreateView.as_view(), name='tag_create'),
    path('tag/<str:slug>/update/', TagUpdateView.as_view(), name='tag_update'),
    path('tag/<str:slug>/', TagDetailView.as_view(), name='tag_detail'),

]