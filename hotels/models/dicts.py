from common.models.dicts import BaseDictModelMixin, ExtendedDictModelMixin


class AccommodationType(BaseDictModelMixin):
    class Meta:
        verbose_name = 'Тип размещения'
        verbose_name_plural = 'Типы размещений'


class RoomStatus(ExtendedDictModelMixin):

    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'
