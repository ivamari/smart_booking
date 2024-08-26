from django.db import models


class Hotel(models.Model):
    name = models.CharField('Название', max_length=64)
    address = models.CharField('Адрес', max_length=64)
    description = models.TextField('Описание', null=True, blank=True)

    class Meta:
        verbose_name = 'Отель'
        verbose_name_plural = 'Отели'

    def __str__(self):
        return f'{self.pk} - {self.name}'
