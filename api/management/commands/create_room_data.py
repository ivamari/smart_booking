from django.core.management.base import BaseCommand
from django.db.models import Q

from hotels.models.rooms import HotelRoom
from hotels.services.creators.rooms import HotelRoomCreatorService


class Command(BaseCommand):
    help = 'Добавить недостающие данные о номерах отеля'

    def handle(self, *args, **kwargs):
        rooms = HotelRoom.objects.filter(Q(settings__isnull=True) |
                                         Q(status__isnull=True))
        for room in rooms:
            settings, status = HotelRoomCreatorService().create_dependencies(
                room)
            if settings:
                self.stdout.write(self.style.SUCCESS(
                    f'Добавлены настройки для комнаты: {room.id}'))
            if status:
                self.stdout.write(self.style.SUCCESS(
                    f'Добавлен статус для комнаты: {room.id}'))
