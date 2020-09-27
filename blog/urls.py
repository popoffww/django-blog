from django.urls import path
from .views import *

urlpatterns = [
    path('', HomeListView.as_view(), name='home'),
    path('posts/', PostListView.as_view(), name='posts'),
    path('post/<str:slug>/', PostDetailView.as_view(), name='post_detail'),
    path('tags/', TagListView.as_view(), name='tags'),
    path('tag/<str:slug>/', TagDetail.as_view(), name='tag_detail'),

]