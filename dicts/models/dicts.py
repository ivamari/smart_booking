from django.db import models

from common.models.dicts import BaseDictModelMixin


class Gender(BaseDictModelMixin):
    class Meta:
        verbose_name = 'Гендер'
        verbose_name_plural = 'Гендеры'


class AgeType(models.Model):
    name = models.CharField('Название', max_length=10)
    age_from = models.IntegerField('Минимальный возраст')
    age_to = models.IntegerField('Максимальный возраст')

    class Meta:
        verbose_name = 'Диапазон возраста'
        verbose_name_plural = 'Диапазоны возрастов'

    def __str__(self):
        return f'{self.name}({self.age_from} - {self.age_to})'


