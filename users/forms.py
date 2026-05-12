from django import forms
from . import models
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class RegisterForm(UserCreationForm):

    class Meta:
        model = models.CustomUser

        fields = [
            'username',
            'email',
            'phone',
            'age',
            'city',
            'education',
            'experience',
            'skills',
            'desired_position',
            'salary',
            'resume',
            'photo',
            'password1',
            'password2',
        ]



class LoginForm(AuthenticationForm):

    captcha = forms.CharField(
        label='Введите текст: Я не робот',
    )

    def clean_captcha(self):

        value = self.cleaned_data['captcha']

        if value != 'Я не робот':
            raise forms.ValidationError('Неправильная капча')

        return value 