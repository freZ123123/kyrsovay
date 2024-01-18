from django.db import models


class Fish(models.Model):
    fish = models.CharField('Название', max_length=50)
    fif = models.TextField(verbose_name = 'Описание', default='')
    Price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='static/fish_images/')


class Meta:
    verbose_name = 'Ассортимент'
    verbose_name_plural = 'Ассортимент'


class user(models.Model):
    name = models.CharField('Название', max_length=50)
    email = models.CharField('Название', max_length=50)
    accounts = models.CharField('Название', max_length=50)


class Meta:
    verbose_name = 'Форма'
    verbose_name_plural = 'Форма'

