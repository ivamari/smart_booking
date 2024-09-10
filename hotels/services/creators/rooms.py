from hotels.models.rooms import HotelRoom, HotelRoomSettings, HotelRoomStatus


class HotelRoomCreatorService:

    def create_instance(self, validated_data):
        room = HotelRoom.objects.create(**validated_data)

        if not getattr(room, 'settings', None):
            HotelRoomSettings.objects.create(room=room)

        if not getattr(room, 'status', None):
            HotelRoomStatus.objects.create(room=room, status_id='created')

        return room

    def create_dependencies(self, room):

        created_settings = False
        created_status = False

        if not getattr(room, 'settings', None):
            HotelRoomSettings.objects.create(room=room)
            created_settings = True

        if not getattr(room, 'status', None):
            HotelRoomStatus.objects.create(room=room, status_id='created')
            created_status = True

        return created_settings, created_status
