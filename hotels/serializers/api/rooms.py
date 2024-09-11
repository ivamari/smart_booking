from rest_framework import serializers

from common.serializers.mixins import ExtendedModelSerializer
from hotels.models.hotels import Hotel
from hotels.models.rooms import HotelRoom
from hotels.serializers.api.dicts import AccommodationTypeGetSerializer
from hotels.serializers.nested.rooms import (HotelRoomSettingsSerializer,
                                             HotelRoomStatusSerializer)
from hotels.services.creators.rooms import HotelRoomCreatorService


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


class RoomCreateSerializer(ExtendedModelSerializer):
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
        hotel_id = self.get_value_from_url('id')
        self.get_object_from_model(hotel_id, Hotel, 'id', raise_not_found=True)

        attrs['hotel_id'] = hotel_id

        attrs['max_guests'] = attrs['accommodation_type'].max_guests
        attrs['max_adults'] = attrs['accommodation_type'].max_adults
        attrs['max_children'] = attrs['accommodation_type'].max_children
        attrs['private'] = attrs['accommodation_type'].private

        return attrs

    def create(self, validated_data):
        return HotelRoomCreatorService().create_instance(validated_data)


class RoomUpdateSerializer(ExtendedModelSerializer):
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
        hotel_id = self.get_value_from_url('id')
        attrs['hotel_id'] = hotel_id
        return attrs
