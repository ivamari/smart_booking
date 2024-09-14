from common.models.dicts import ExtendedDictModelMixin


class ReservationStatus(ExtendedDictModelMixin):
    class Meta:
        verbose_name = 'Статус бронирования'
        verbose_name_plural = 'Статусы бронирований'

    def __str__(self):
        return self.code


class ReservationRoomStatus(ExtendedDictModelMixin):
    class Meta:
        verbose_name = 'Статус бронирования комнаты'
        verbose_name_plural = 'Статусы бронирований комнат'

    def __str__(self):
        return self.code
