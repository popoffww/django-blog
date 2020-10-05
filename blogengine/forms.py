from django import forms
from django.contrib.auth.hashers import check_password
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model, authenticate
User = get_user_model()


class UserLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username').strip()
        password = self.cleaned_data.get('password').strip()
        if username and password:
            qs = User.objects.filter(username=username)
        if not qs.exists():
            raise forms.ValidationError('Такого пользователя нет!')
        if not check_password(password, qs[0].password):
            raise forms.ValidationError('Пароль не верный!')
        user = authenticate(username=username, password=password)
        if not user:
            raise forms.ValidationError('Данный аккаунт отключен')
