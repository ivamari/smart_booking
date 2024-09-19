from rest_framework.exceptions import ValidationError

from reservations.models.reservations import Reservation


def validate_reservation_dates(attrs, instance=None):
    if instance:
        existing_reservation = Reservation.objects.filter(client=
                                                          instance.client).filter(
            start_date__lte=attrs['end_date']).exclude(id=instance.id).first()
    else:
        existing_reservation = Reservation.objects.filter(
            client=attrs['client']).filter(
            start_date__lte=attrs['end_date']).first()

    if existing_reservation is None:
        raise ValidationError(f'Указанный гость уже имеет бронирование №'
                              f'{existing_reservation.pk} в выбранные даты')


def validate_total_quests(attrs):
    rooms = attrs['rooms']
    total_number_rooms = 0

    for room in rooms:
        total_number_rooms += room.max_adults + room.max_children
        print(total_number_rooms)

    if total_number_rooms < (attrs['adults'] + attrs['children']):
        raise ValidationError('Количество гостей не совпадает '
                              'с общим количеством мест в комнатах')


def validate_status(attrs, instance):
    if instance.status_id in ('checked_in', 'checked_out', 'cancelled',
                              'no_show'):
        if instance.rooms != attrs['rooms']:
            raise ValidationError(f'Нельзя изменять '
                                  f'массив комнат при статусе '
                                  f'бронирования {instance.status}')
