from rest_framework import serializers

from hotels.models.dicts import RoomStatus


class RoomStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomStatus
        fields = (
            'code',
            'name',
            'color',
        )
