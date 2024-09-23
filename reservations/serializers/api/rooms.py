from rest_framework import serializers

from common.serializers.mixins import ExtendedModelSerializer
from hotels.models.rooms import HotelRoom
from reservations.models.dicts import ReservationRoomStatus
from reservations.models.reservations import ReservationRoom, Reservation
from reservations.serializers.nested.dicts import ReservationStatusSerializer
from reservations.serializers.nested.rooms import HotelRoomShortSerializer
from reservations.validators import validate_reservations_room


class ReservationRoomListSerializer(ExtendedModelSerializer):
    room = HotelRoomShortSerializer()
    status = ReservationStatusSerializer()

    class Meta:
        model = ReservationRoom
        fields = (
            'room',
            'status',
        )


class ReservationRoomRetrieveSerializer(ExtendedModelSerializer):
    room = HotelRoomShortSerializer()
    status = ReservationStatusSerializer()

    class Meta:
        model = ReservationRoom
        fields = (
            'room',
            'status',
        )


class ReservationRoomCreateSerializer(ExtendedModelSerializer):
    room = serializers.PrimaryKeyRelatedField(queryset=HotelRoom.objects.all())
    reservation = serializers.CharField(read_only=True)
    status = serializers.CharField(read_only=True)

    class Meta:
        model = ReservationRoom
        fields = (
            'id',
            'room',
            'reservation',
            'status',
        )

    def validate(self, attrs):
        attrs['status'] = ReservationRoomStatus.objects.get(
            code='not_checked_in')
        reservation = Reservation.objects.get(id=self.get_value_from_url('id'))
        attrs['reservation'] = reservation

        validate_reservations_room(attrs['room'], reservation)

        return attrs


class ReservationRoomUpdateSerializer(ExtendedModelSerializer):
    status = serializers.PrimaryKeyRelatedField(
        queryset=ReservationRoomStatus.objects.all())

    class Meta:
        model = ReservationRoom
        fields = (
            'id',
            'status',
        )
