from django.db import models

from clients.models.clients import Client
from common.models.dicts import InfoMixin
from hotels.models.rooms import HotelRoom
from reservations.models.dicts import ReservationStatus, ReservationRoomStatus


class Reservation(InfoMixin):
    status = models.ForeignKey(ReservationStatus, models.RESTRICT,
                               'reservations', verbose_name='Статус')
    client = models.ForeignKey(Client, models.CASCADE, 'reservations',
                               verbose_name='Клиент')
    client_name = models.CharField('Имя гостя', max_length=64)
    start_date = models.DateField('Дата заселения')
    end_date = models.DateField('Дата выселения')
    adults = models.IntegerField('Количество взрослых')
    children = models.IntegerField('Количество детей')
    rooms = models.ManyToManyField(HotelRoom, through='ReservationRoom')

    class Meta:
        verbose_name = 'Бронирование'
        verbose_name_plural = 'Бронирования'

    def __str__(self):
        return f'{self.client_name} - {self.status}'


class ReservationClient(models.Model):
    reservation = models.OneToOneField(Reservation, models.CASCADE,
                                       related_name='reservation_client',
                                       verbose_name='Бронирование')
    client = models.ForeignKey(Client, models.CASCADE,
                               related_name='reservation',
                               verbose_name='Клиент')
    checked = models.BooleanField('Проверено', default=False)
    is_main_client = models.BooleanField('Основной клиент',
                                         default=False)

    class Meta:
        verbose_name = 'Бронирование клиента'
        verbose_name_plural = 'Бронирования клиентов'

    def __str__(self):
        return f'Бронирование клиента {self.client}'


class ReservationRoom(models.Model):
    reservation = models.ForeignKey(Reservation, models.CASCADE,
                                    'reservation_rooms',
                                    verbose_name='Бронирование')
    room = models.ForeignKey(HotelRoom, models.CASCADE, 'reservations',
                             verbose_name='Комната')
    status = models.ForeignKey(ReservationRoomStatus, models.RESTRICT,
                               'rooms', verbose_name='Статус')

    class Meta:
        verbose_name = 'Бронирование комнаты'
        verbose_name_plural = 'Бронирования комнат'

    def __str__(self):
        return f'{self.room} - {self.status}'
