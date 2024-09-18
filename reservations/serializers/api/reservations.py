from rest_framework import serializers

from clients.models.clients import Client
from hotels.models.rooms import HotelRoom
from reservations.models.dicts import ReservationStatus
from reservations.models.reservations import Reservation
from reservations.serializers.nested.clients import ClientSerializer
from reservations.serializers.nested.dicts import ReservationStatusSerializer
from reservations.serializers.nested.reservations import (
    ReservationClientSerializer, ReservationRoomSerializer)
from reservations.services.creators.reservations import \
    ReservationCreatorService
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


class ReservationCreateSerializer(serializers.ModelSerializer):
    client = serializers.PrimaryKeyRelatedField(queryset=Client.objects.all())
    rooms = serializers.PrimaryKeyRelatedField(queryset=HotelRoom.objects.all(),
                                               many=True)

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

    def validate(self, attrs):
        attrs['client_name'] = attrs['client'].full_name
        attrs['status'] = ReservationStatus.objects.get(code='not_confirmed')
        return attrs

    def create(self, validated_data):
        return ReservationCreatorService().create_instance(validated_data)
