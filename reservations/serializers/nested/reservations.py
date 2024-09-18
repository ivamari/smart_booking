from rest_framework import serializers
from reservations.models.reservations import (ReservationClient,
                                              ReservationRoom)
from reservations.serializers.nested.clients import ClientSerializer
from reservations.serializers.nested.dicts import ReservationStatusSerializer
from reservations.serializers.nested.rooms import HotelRoomShortSerializer


class ReservationClientSerializer(serializers.ModelSerializer):
    client = ClientSerializer()

    class Meta:
        model = ReservationClient
        fields = (
            'client',
            'checked',
            'is_main_client',
        )


class ReservationRoomSerializer(serializers.ModelSerializer):
    room = HotelRoomShortSerializer()
    status = ReservationStatusSerializer()

    class Meta:
        model = ReservationRoom
        fields = (
            'room',
            'status'
        )
