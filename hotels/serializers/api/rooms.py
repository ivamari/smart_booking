from rest_framework import serializers

from hotels.models.rooms import HotelRoom
from hotels.serializers.api.dicts import AccommodationTypeGetSerializer
from hotels.serializers.nested.rooms import HotelRoomSettingsSerializer, \
    HotelRoomStatusSerializer


class RoomListSerializer(serializers.ModelSerializer):
    accommodation_type = AccommodationTypeGetSerializer()
    settings = HotelRoomSettingsSerializer()
    status_info = HotelRoomStatusSerializer(source='room_status')

    class Meta:
        model = HotelRoom
        fields = (
            'id',
            'number',
            'floor',
            'accommodation_type',
            'description',
            'settings',
            'status_info',
        )


class RoomRetrieveSerializer(serializers.ModelSerializer):
    accommodation_type = AccommodationTypeGetSerializer()
    settings = HotelRoomSettingsSerializer()
    status_info = HotelRoomStatusSerializer(source='room_status')

    class Meta:
        model = HotelRoom
        fields = (
            'id',
            'number',
            'floor',
            'accommodation_type',
            'description',
            'settings',
            'status_info',
        )


class RoomCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelRoom
        fields = (
            'id',
            'number',
            'floor',
            'accommodation_type',
            'description',
        )

    def validate(self, attrs):
        hotel_id = self.context['view'].kwargs.get('id')
        attrs['hotel_id'] = hotel_id
        return attrs


class RoomUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelRoom
        fields = (
            'id',
            'number',
            'floor',
            'accommodation_type',
            'description',
        )

    def validate(self, attrs):
        hotel_id = self.context['view'].kwargs.get('id')
        attrs['hotel_id'] = hotel_id
        return attrs
