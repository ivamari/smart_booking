from django.db import models

from common.models.dicts import BaseDictModelMixin, ExtendedDictModelMixin


class AccommodationType(BaseDictModelMixin):
    description = models.TextField('Описание', null=True, blank=True)
    private = models.BooleanField('Приватный', default=False)
    max_guests = models.IntegerField('Кол-во гостей')
    max_adults = models.IntegerField('Кол-во подростков')
    max_children = models.IntegerField('Кол-во детей')

    class Meta:
        verbose_name = 'Тип размещения'
        verbose_name_plural = 'Типы размещений'


class RoomStatus(ExtendedDictModelMixin):
    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'
