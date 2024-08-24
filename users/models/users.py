from django.db import models

from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from transliterate import translit

from users.managers import CustomUserManager


class User(AbstractUser):
    first_name = models.CharField('Имя', max_length=64)
    last_name = models.CharField('Фамилия', max_length=64)
    middle_name = models.CharField('Отчество', max_length=64, null=True,
                                   blank=True)
    dob = models.DateField('Дата рождения', null=True, blank=True)
    email = models.EmailField('Почта', unique=True, null=True, blank=True)
    phone = PhoneNumberField('Телефон')

    USERNAME_FIELD = 'username'

    objects = CustomUserManager()

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    @property
    def full_name(self):
        return f'{self.last_name} {self.first_name}{" " + self.middle_name if self.middle_name else ""}'

    def __str__(self):
        return f'{self.full_name}'
