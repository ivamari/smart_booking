from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Hotel(models.Model):
    name = models.CharField('Название', max_length=64)
    address = models.CharField('Адрес', max_length=64)
    description = models.TextField('Описание', null=True, blank=True)
    phone = PhoneNumberField('Телефон', null=True, blank=True)
    email = models.EmailField('Email', null=True, blank=True)

    class Meta:
        verbose_name = 'Отель'
        verbose_name_plural = 'Отели'

    def __str__(self):
        return f'{self.name} ({self.pk})'


class HotelPolicy(models.Model):
    hotel = models.OneToOneField(Hotel, models.CASCADE, verbose_name='Отель',
                                 primary_key=True, unique=True)
    check_in = models.TimeField('Время заселения')
    check_out = models.TimeField('Время выселения')

    class Meta:
        verbose_name = 'Политика отеля'
        verbose_name_plural = 'Политики отелей'
