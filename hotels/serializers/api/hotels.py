from rest_framework import serializers

from hotels.models.hotels import Hotel


class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = (
            'id',
            'name',
            'address',
            'description',
        )
