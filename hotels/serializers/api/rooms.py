from rest_framework import serializers

from hotels.models.rooms import Room
from hotels.serializers.api.dicts import AccommodationTypeGetSerializer


class RoomListSerializer(serializers.ModelSerializer):
    accommodation_type = AccommodationTypeGetSerializer()

    class Meta:
        model = Room
        fields = (
            'id',
            'number',
            'accommodation_type',
            'description',
        )


class RoomRetrieveSerializer(serializers.ModelSerializer):
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
            'number',
            'accommodation_type',
            'description',
        )

    def validate(self, attrs):
        hotel_id = self.context['view'].kwargs.get('id')
        attrs['hotel_id'] = hotel_id
        return attrs


class RoomUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = (
            'id',
            'number',
            'accommodation_type',
            'description',
        )

    def validate(self, attrs):
        hotel_id = self.context['view'].kwargs.get('id')
        attrs['hotel_id'] = hotel_id
        return attrs
