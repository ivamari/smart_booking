from rest_framework import serializers

from hotels.models.dicts import AccommodationType
from hotels.models.rooms import HotelRoom
from hotels.serializers.api.dicts import AccommodationTypeGetSerializer
from hotels.serializers.nested.rooms import (HotelRoomSettingsSerializer,
                                             HotelRoomStatusSerializer)


class RoomListSerializer(serializers.ModelSerializer):
    accommodation_type = AccommodationTypeGetSerializer()
    settings = HotelRoomSettingsSerializer()
    status_info = HotelRoomStatusSerializer(source='status')

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
            'max_guests',
            'max_adults',
            'max_children',
            'description',
        )


class RoomRetrieveSerializer(serializers.ModelSerializer):
    accommodation_type = AccommodationTypeGetSerializer()
    settings = HotelRoomSettingsSerializer()
    status_info = HotelRoomStatusSerializer(source='status')

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
            'max_guests',
            'max_adults',
            'max_children',
            'description',
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

        accommodation_type = AccommodationType.objects.get(
            code=attrs['accommodation_type'])
        attrs['max_guests'] = accommodation_type.max_guests
        attrs['max_adults'] = accommodation_type.max_adults
        attrs['max_children'] = accommodation_type.max_children
        attrs['private'] = accommodation_type.private

        return attrs


class RoomUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = HotelRoom
        fields = (
            'number',
            'floor',
            'accommodation_type',
            'description',
            'max_guests',
            'max_adults',
            'max_children',
            'private',
        )

    def validate(self, attrs):
        hotel_id = self.context['view'].kwargs.get('id')
        attrs['hotel_id'] = hotel_id
        return attrs
