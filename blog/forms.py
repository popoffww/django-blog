from django import forms
from django.core.exceptions import ValidationError
from .models import *

class TagForm(forms.ModelForm):
    title = forms.CharField(label='Тэг',
                            widget=forms.TextInput(
                            attrs={'class': 'form-control', 'placeholder': 'Введите тэг'}))
    slug = forms.CharField(label='Слаг',
                           widget=forms.TextInput(
                           attrs={'class': 'form-control', 'placeholder': 'Введите слаг'}))

    class Meta(object):
        model = Tag
        fields = ('title', 'slug')


    def clean_slug(self):
        new_slug = self.cleaned_data['slug'].lower()
        if new_slug == 'create':
            raise ValidationError('Слаг не может быть "create"')
        if Tag.objects.filter(slug__iexact=new_slug).count():
            raise ValidationError('Слаг должен быть уникальным. Слаг "{}" уже существует'.format(new_slug))
        return new_slug
    