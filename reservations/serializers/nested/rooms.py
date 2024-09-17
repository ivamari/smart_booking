from rest_framework import serializers

from hotels.models.rooms import HotelRoom


class HotelRoomShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelRoom
        fields = (
            'number',
            'floor',
            'accommodation_type',
            'private',
        )
