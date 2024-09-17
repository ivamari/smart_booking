from rest_framework import serializers

from reservations.models.reservations import Reservation
from reservations.serializers.nested.clients import ClientSerializer
from reservations.serializers.nested.dicts import ReservationStatusSerializer
from reservations.serializers.nested.reservations import (
    ReservationClientSerializer, ReservationRoomSerializer)
from users.serializers.nested.users import UserShortSerializer


class ReservationListSerializer(serializers.ModelSerializer):
    status = ReservationStatusSerializer()
    client = ClientSerializer()
    created_by = UserShortSerializer()
    updated_by = UserShortSerializer()
    clients = ReservationClientSerializer(many=True)
    rooms = ReservationRoomSerializer(many=True)

    class Meta:
        model = Reservation
        fields = (
            'id',
            'status',
            'client',
            'client_name',
            'start_date',
            'end_date',
            'adults',
            'children',
            'created_at',
            'updated_at',
            'created_by',
            'updated_by',
            'clients',
            'rooms',
        )


class ReservationRetrieveSerializer(serializers.ModelSerializer):
    status = ReservationStatusSerializer()
    client = ClientSerializer()
    created_by = UserShortSerializer()
    updated_by = UserShortSerializer()
    clients = ReservationClientSerializer(many=True)
    rooms = ReservationRoomSerializer(many=True)

    class Meta:
        model = Reservation
        fields = (
            'id',
            'status',
            'client',
            'client_name',
            'start_date',
            'end_date',
            'adults',
            'children',
            'created_at',
            'updated_at',
            'created_by',
            'updated_by',
            'clients',
            'rooms',
        )


class ReservationRCreateSerializer(serializers.ModelSerializer):
    status = ReservationStatusSerializer()
    client = ClientSerializer()
    created_by = UserShortSerializer()
    updated_by = UserShortSerializer()
    clients = ReservationClientSerializer(many=True)
    rooms = ReservationRoomSerializer(many=True)

    class Meta:
        model = Reservation
        fields = (
            'client',
            'start_date',
            'end_date',
            'adults',
            'children',
            'rooms',
        )
