from rest_framework.exceptions import ValidationError

from reservations.models.reservations import Reservation, ReservationRoom


def validate_reservation_dates(attrs, instance=None):
    if instance:
        existing_reservation = Reservation.objects.filter(
            client=instance.client
        ).filter(
            start_date__lte=attrs['end_date'],
            end_date__gte=attrs['start_date']
        ).exclude(id=instance.id).first()

    else:
        existing_reservation = Reservation.objects.filter(
            client=attrs['client']
        ).filter(
            start_date__lte=attrs['end_date'],
            end_date__gte=attrs['start_date']
        ).first()

    if existing_reservation is not None:
        print(existing_reservation)
        raise ValidationError(f'Указанный гость уже имеет бронирование №'
                              f'{existing_reservation.id} в выбранные даты')


def validate_total_quests(attrs):
    rooms = attrs['rooms']
    total_number_rooms = 0

    for room in rooms:
        total_number_rooms += room.max_adults + room.max_children

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


def validate_reservations_room(room, reservation, instance=None):
    end_date = reservation.end_date
    start_date = reservation.start_date

    existing_reservations_room = ReservationRoom.objects.filter(
        room=room
    ).filter(
        reservation__start_date__lte=end_date,
        reservation__end_date__gte=start_date
    ).first()

    if existing_reservations_room is not None:
        raise ValidationError(f'Комната уже имеет бронирование в период c '
                              f'{start_date} по {end_date}')

