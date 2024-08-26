from django.utils import timezone
from dateutil.relativedelta import relativedelta
from rest_framework.exceptions import ParseError


def validate_dob(value):
    now = timezone.now().date()
    age = relativedelta(now, value).years

    if not 0 < age < 100:
        raise ParseError('Проверьте дату рождения')

    return value
