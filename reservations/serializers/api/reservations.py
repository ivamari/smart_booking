from rest_framework import serializers

from hotels.models.rooms import HotelRoom
from reservations.services.updaters.reservations import ReservationUpdateService
from reservations.validators import (validate_reservation_dates,
                                     validate_total_quests, validate_status)
from reservations.models.dicts import ReservationStatus
from reservations.models.reservations import Reservation
from reservations.serializers.nested.clients import ClientSerializer
from reservations.serializers.nested.dicts import ReservationStatusSerializer
from reservations.services.creators.reservations import (
    ReservationCreatorService)
from users.serializers.nested.users import UserShortSerializer


class ReservationListSerializer(serializers.ModelSerializer):
    status = ReservationStatusSerializer()
    client = ClientSerializer()
    created_by = UserShortSerializer()
    updated_by = UserShortSerializer()

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
        )


class ReservationRetrieveSerializer(serializers.ModelSerializer):
    status = ReservationStatusSerializer()
    client = ClientSerializer()
    created_by = UserShortSerializer()
    updated_by = UserShortSerializer()

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
        )


class ReservationCreateSerializer(serializers.ModelSerializer):
    rooms = serializers.PrimaryKeyRelatedField(queryset=HotelRoom.objects.all(),
                                               many=True, write_only=True)

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

        validate_reservation_dates(attrs)
        validate_total_quests(attrs)

        return attrs

    def create(self, validated_data):
        return ReservationCreatorService().create_instance(validated_data)


class ReservationUpdateSerializer(serializers.ModelSerializer):
    rooms = serializers.PrimaryKeyRelatedField(queryset=HotelRoom.objects.all(),
                                               write_only=True,
                                               many=True)

    class Meta:
        model = Reservation
        fields = (
            'start_date',
            'end_date',
            'adults',
            'children',
            'rooms',
        )

    def validate(self, attrs):
        validate_reservation_dates(attrs, self.instance)
        validate_total_quests(attrs)
        validate_status(attrs, self.instance)

        return attrs

    def update(self, instance, validated_data):
        return ReservationUpdateService().update_instance(validated_data,
                                                          instance)
