from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from dicts.models.dicts import Gender


class Client(models.Model):
    first_name = models.CharField('Имя', max_length=64)
    last_name = models.CharField('Фамилия', max_length=64)
    middle_name = models.CharField('Отчество', max_length=64, null=True,
                                   blank=True)
    dob = models.DateField('Дата рождения', null=True, blank=True)
    email = models.EmailField('Почта', unique=True, null=True, blank=True)
    phone = PhoneNumberField('Телефон', unique=True, null=True, blank=True)
    gender = models.ForeignKey(Gender, verbose_name='Гендер', null=True,
                               related_name='clients',
                               on_delete=models.SET_NULL)

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'

    @property
    def full_name(self):
        return f'{self.last_name} {self.first_name}{" " + self.middle_name if self.middle_name else ""}'

    def __str__(self):
        return f'{self.full_name}'
