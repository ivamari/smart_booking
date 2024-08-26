from django.db import models

from hotels.models.dicts import AccommodationType
from hotels.models.hotels import Hotel


class Room(models.Model):
    hotel = models.ForeignKey(Hotel, verbose_name='Отель',
                              related_name='hotel_rooms',
                              on_delete=models.CASCADE)
    number = models.IntegerField('Номер комнаты')
    accommodation_type = models.ForeignKey(AccommodationType,
                                           verbose_name='Тип размещения',
                                           related_name='accommodation_type_rooms',
                                           on_delete=models.SET_NULL,
                                           null=True)
    description = models.TextField('Описание')

    class Meta:
        verbose_name = 'Комната'
        verbose_name_plural = 'Комнаты'

    def __str__(self):
        return f'{self.number} ({self.hotel}, {self.accommodation_type})'
