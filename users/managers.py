from django.contrib.auth.base_user import BaseUserManager
from rest_framework.exceptions import ParseError
from transliterate import translit


class CustomUserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, first_name=None, last_name=None, password=None,
                     username=None, **extra_fields):
        if not first_name:
            raise ParseError('Укажите имя')

        if not last_name:
            raise ParseError('Укажите фамилию')

        if not username:
            if last_name and not username:
                username = translit(str(last_name), 'ru',
                                    reversed=True).lower()

        user = self.model(username=username, **extra_fields)

        user.first_name = first_name
        user.last_name = last_name

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, first_name=None, last_name=None, password=None,
                    username=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_active', True)

        return self._create_user(
            first_name, last_name, password, username, **extra_fields
        )

    def create_superuser(self, phone_number=None, email=None, password=None,
                         username=None, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)

        if not (email or phone_number or username):
            raise ParseError('Укажите email или телефон')

        if email:
            email = self.normalize_email(email)

        if not username:
            if email:
                username = email
            else:
                username = phone_number

        user = self.model(username=username, **extra_fields)
        if email:
            user.email = email
        if phone_number:
            user.phone_number = phone_number

        user.set_password(password)
        user.save(using=self._db)
        return user
