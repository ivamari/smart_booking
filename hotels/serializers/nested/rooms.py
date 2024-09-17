from rest_framework import serializers

from hotels.models.rooms import HotelRoomSettings, HotelRoomStatus
from hotels.serializers.nested.dicts import RoomStatusSerializer
from users.serializers.nested.users import UserShortSerializer


class HotelRoomSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelRoomSettings
        fields = (
            'has_airconditioner',
            'has_tv',
            'has_wifi',
        )


class HotelRoomStatusSerializer(serializers.ModelSerializer):
    status = RoomStatusSerializer()
    updated_by = UserShortSerializer()

    class Meta:
        model = HotelRoomStatus
        fields = (
            'status',
            'updated_at',
            'updated_by'
        )


