from rest_framework import serializers

from hotels.models.rooms import Room
from hotels.serializers.api.dicts import AccommodationTypeGetSerializer


class RoomGetSerializer(serializers.ModelSerializer):
    accommodation_type = AccommodationTypeGetSerializer()

    class Meta:
        model = Room
        fields = (
            'id',
            'number',
            'accommodation_type',
            'description',
        )


class RoomCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = (
            'id',
            'name',
            'accommodation_type',
            'description',
        )


class RoomUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = (
            'id',
            'name',
            'accommodation_type',
            'description',
        )
