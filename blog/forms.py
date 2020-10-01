from django import forms
from django.core.exceptions import ValidationError
from .models import *


class PostForm(forms.ModelForm):
    draft = forms.BooleanField(label='Черновик', required=False)

    class Meta:
        model = Post
        fields = ['title', 'slug', 'body', 'tags', 'draft']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите тэг'}),
            'slug': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите слаг'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Текст поста'}),
            'tags': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }

    def clean_slug(self):
        new_slug = self.cleaned_data['slug'].lower()
        if new_slug == 'create':
            raise ValidationError('Слаг не может быть "create"')
        return new_slug


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['title', 'slug']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите тэг'}),
            'slug': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите слаг'}),
        }

    def clean_slug(self):
        new_slug = self.cleaned_data['slug'].lower()
        if new_slug == 'create':
            raise ValidationError('Слаг не может быть "create"')
        if Tag.objects.filter(slug__iexact=new_slug).count():
            raise ValidationError('Слаг должен быть уникальным. Слаг "{}" уже существует'.format(new_slug))
        return new_slug
