from django.db import models
from django.shortcuts import reverse
from django.utils.text import slugify
from time import time
from datetime import datetime

def gen_slug(s):
    new_slug = slugify(s, allow_unicode=True)
    return new_slug + '-' + str(int(time()))

class Post(models.Model):
    title = models.CharField('Заголовок', max_length=150, db_index=True)
    slug = models.SlugField('Слаг', max_length=150, blank=True, unique=True)
    body = models.TextField('Текст поста', blank=True, db_index=True)
    tags = models.ManyToManyField('Tag', blank=True, related_name='posts', verbose_name='Тэги')
    date_pub = models.DateField('Дата', auto_now_add=True)
    draft = models.BooleanField('Черновик', unique=False)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = gen_slug(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'slug': self.slug})

    def get_update_url(self):
        return reverse('post_update', kwargs={'slug': self.slug})

    def get_remove_url(self):
        return reverse('post_remove', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Статья блога'
        verbose_name_plural = 'Статьи блога'

class Tag(models.Model):
    title = models.CharField('Тэг', max_length=50)
    slug = models.CharField('Слаг', max_length=50, unique=True)

    def __str__(self):
            return self.title

    def get_absolute_url(self):
        return reverse('tag_detail', kwargs={'slug': self.slug})

    def get_update_url(self):
        return reverse('tag_update', kwargs={'slug': self.slug})

    def get_remove_url(self):
        return reverse('tag_remove', kwargs={'slug': self.slug})


        


