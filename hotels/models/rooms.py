from django.db import models

from common.models.dicts import InfoMixin
from hotels.models.dicts import AccommodationType, RoomStatus
from hotels.models.hotels import Hotel


class HotelRoom(models.Model):
    hotel = models.ForeignKey(Hotel, models.CASCADE, 'rooms')
    number = models.IntegerField('Номер комнаты')
    floor = models.PositiveSmallIntegerField('Этаж')
    accommodation_type = models.ForeignKey(AccommodationType,
                                           models.RESTRICT,
                                           'rooms')
    description = models.TextField('Описание', null=True, blank=True)
    max_guests = models.IntegerField('Кол-во гостей')
    max_adults = models.IntegerField('Кол-во взрослых')
    max_children = models.IntegerField('Кол-во детей')
    private = models.BooleanField('Приватный', default=False)

    class Meta:
        verbose_name = 'Номер отеля'
        verbose_name_plural = 'Номера отеля'

    def __str__(self):
        return f'{self.number} ({self.hotel}, {self.accommodation_type})'


class HotelRoomStatus(InfoMixin):
    room = models.OneToOneField(HotelRoom, models.CASCADE,
                                related_name='status',
                                verbose_name='Номер отеля',
                                primary_key=True)
    status = models.ForeignKey(RoomStatus, models.RESTRICT, 'info_status',
                               verbose_name='Статус номера отеля')

    class Meta:
        verbose_name = 'Статус номера отеля'
        verbose_name_plural = 'Статусы номеров отеля'

    def __str__(self):
        return f'{self.room} - {self.status}'


class HotelRoomSettings(models.Model):
    room = models.OneToOneField(HotelRoom, models.CASCADE,
                                related_name='settings',
                                primary_key=True, verbose_name='Номер отеля', )
    has_airconditioner = models.BooleanField('Наличие кондиционера',
                                             default=False)
    has_tv = models.BooleanField('Наличие телевизора', default=False)
    has_wifi = models.BooleanField('Наличие Wi-Fi', default=False)

    class Meta:
        verbose_name = 'Параметры номера отеля'
        verbose_name_plural = 'Параметры номеров отеля'

    def __str__(self):
        return f'Параметры номера {self.room}'
