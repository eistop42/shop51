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