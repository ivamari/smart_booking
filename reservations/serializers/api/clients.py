from rest_framework import serializers

from common.serializers.mixins import ExtendedModelSerializer
from reservations.factories.clients import ReservationClientFactory
from reservations.models.reservations import (Reservation,
                                              ReservationClient)
from reservations.serializers.nested.clients import ClientSerializer


class ReservationClientListSerializer(ExtendedModelSerializer):
    client = ClientSerializer()

    class Meta:
        model = ReservationClient
        fields = (
            'id',
            'client',
            'checked',
            'is_main_client',
        )


class ReservationClientRetrieveSerializer(ExtendedModelSerializer):
    client = ClientSerializer()

    class Meta:
        model = ReservationClient
        fields = (
            'id',
            'client',
            'checked',
            'is_main_client',
        )


class ReservationClientCreateSerializer(ExtendedModelSerializer):
    reservation = serializers.CharField(read_only=True)
    checked = serializers.BooleanField(read_only=True)
    is_main_client = serializers.BooleanField(read_only=True)

    class Meta:
        model = ReservationClient
        fields = (
            'id',
            'client',
            'reservation',
            'checked',
            'is_main_client',
        )

    def validate(self, attrs):

        if ReservationClient.objects.filter(client=attrs['client']).exists():
            raise serializers.ValidationError('Клиент уже имеет бронирование.')

        attrs['checked'] = False
        attrs['is_main_client'] = False
        reservation = Reservation.objects.get(id=self.get_value_from_url('id'))
        attrs['reservation'] = reservation

        return attrs


class ReservationClientUpdateSerializer(ExtendedModelSerializer):
    reservation = serializers.CharField(read_only=True)
    client = ClientSerializer(read_only=True)

    class Meta:
        model = ReservationClient
        fields = (
            'id',
            'client',
            'reservation',
            'checked',
            'is_main_client',
        )

    def validate(self, attrs):
        ReservationClientFactory().set_client_as_main(self.instance)
        return attrs