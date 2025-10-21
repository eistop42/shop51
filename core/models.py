from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название')
    price = models.IntegerField(verbose_name='Цена')
    count = models.IntegerField(verbose_name='Количество')

    # чтобы отображались красивые названия в админке
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class Filial(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название')
    address = models.CharField(max_length=200, verbose_name='Адрес')
    text = models.TextField(null=True, blank=True, verbose_name='Описание')
    rating = models.IntegerField(default=1, verbose_name='Рейтинг')

    # чтобы отображались красивые названия в админке
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Филиал'
        verbose_name_plural = 'Филиалы'