from django.db import models

from common.models.dicts import InfoMixin
from hotels.models.dicts import AccommodationType, RoomStatus
from hotels.models.hotels import Hotel


class HotelRoom(models.Model):
    hotel = models.ForeignKey(Hotel, verbose_name='Отель',
                              related_name='rooms',
                              on_delete=models.CASCADE)
    number = models.IntegerField('Номер комнаты')
    floor = models.PositiveSmallIntegerField('Этаж')
    accommodation_type = models.ForeignKey(AccommodationType,
                                           verbose_name='Тип размещения',
                                           related_name='rooms',
                                           on_delete=models.SET_NULL,
                                           null=True)
    description = models.TextField('Описание')

    class Meta:
        verbose_name = 'Номер отеля'
        verbose_name_plural = 'Номера отеля'

    def __str__(self):
        return f'{self.number} ({self.hotel}, {self.accommodation_type})'


class HotelRoomStatus(InfoMixin):
    room = models.OneToOneField(HotelRoom, verbose_name='Номер отеля',
                                related_name='room_status',
                                on_delete=models.CASCADE, primary_key=True)
    status = models.ForeignKey(RoomStatus, verbose_name='Статус номера отеля',
                               related_name='info_status',
                               null=True, on_delete=models.SET_NULL)

    class Meta:
        verbose_name = 'Статус номера отеля'
        verbose_name_plural = 'Статусы номеров отеля'

    def __str__(self):
        return f'{self.room} - {self.status}'


class RoomSettings(models.Model):
    room = models.OneToOneField(HotelRoom, verbose_name='Номер отеля',
                                related_name='settings',
                                on_delete=models.CASCADE, primary_key=True)
    has_airconditioner = models.BooleanField('Наличие кондиционера',
                                             default=False)
    has_tv = models.BooleanField('Наличие телевизора', default=False)
    has_wifi = models.BooleanField('Наличие Wi-Fi', default=False)

    class Meta:
        verbose_name = 'Параметры номера отеля'
        verbose_name_plural = 'Параметры номеров отеля'

    def __str__(self):
        return f'Параметры номера {self.room}'
