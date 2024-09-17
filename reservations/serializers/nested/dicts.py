from rest_framework import serializers

from reservations.models.dicts import ReservationStatus


class ReservationStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReservationStatus
        fields = (
            'code',
            'name',
            'color'
        )
