from django.core.management.base import BaseCommand

from hotels.models.dicts import RoomStatus
from hotels.models.rooms import HotelRoom, HotelRoomSettings, HotelRoomStatus


class Command(BaseCommand):
    help = 'Добавить недостающие данные о номерах отеля'

    def handle(self, *args, **kwargs):
        rooms_without_settings = HotelRoom.objects.filter(settings__isnull=True)
        for room in rooms_without_settings:
            HotelRoomSettings.objects.create(room=room)
            self.stdout.write(self.style.SUCCESS(
                f'Добавлены настройки для комнаты: {room.id}'))

        rooms_without_status = HotelRoom.objects.filter(room_status__isnull=True)
        created_status = RoomStatus.objects.get(code='created')
        for room in rooms_without_status:
            HotelRoomStatus.objects.create(room=room, status=created_status)
            self.stdout.write(self.style.SUCCESS(f'Добавлен статус для комнаты: {room.id}'))
