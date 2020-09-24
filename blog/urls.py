from django.urls import path
from .views import home, posts_list, tags_list

urlpatterns = [
    path('', home, name='home'),
    path('posts/', posts_list, name='posts'),
    path('tags/', tags_list, name='tags'),
]