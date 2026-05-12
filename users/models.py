from django.db import models
from django.contrib.auth.models import User

class CustomUser(User):

    phone = models.CharField(max_length=20, verbose_name='Телефон')
    age = models.IntegerField(verbose_name='Возраст')
    city = models.CharField(max_length=100, verbose_name='Город')
    education = models.CharField(max_length=200, verbose_name='Образование')
    experience = models.TextField(verbose_name='Опыт работы')
    skills = models.TextField(verbose_name='Навыки')
    desired_position = models.CharField(max_length=150, verbose_name='Желаемая должность')
    salary = models.IntegerField(verbose_name='Зарплата')
    resume = models.FileField(upload_to='resume/', verbose_name='Резюме')
    photo = models.ImageField(upload_to='photos/', verbose_name='Фото')



    def __str__(self):
        return self.username