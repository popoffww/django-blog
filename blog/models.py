from django.db import models
from django.shortcuts import reverse

class Post(models.Model):
    title = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=150, unique=True)
    body = models.TextField(blank=True, db_index=True)
    tags = models.ManyToManyField('Tag', blank=True, related_name='posts')
    date_pub = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Статья блога'
        verbose_name_plural = 'Статьи блога'

class Tag(models.Model):
    title = models.CharField(max_length=50)
    slug = models.CharField(max_length=50, unique=True)

    def __str__(self):
            return self.title

    def get_absolute_url(self):
        return reverse('tag_detail', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Тэг'
        verbose_name_plural = 'Тэги'
        


