from rest_framework import serializers

from hotels.models.hotels import Hotel


class HotelListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = (
            'id',
            'name',
            'address',
            'description',
        )


class HotelRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = (
            'id',
            'name',
            'address',
            'description',
        )


class HotelCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = (
            'id',
            'name',
            'address',
            'description',
        )


class HotelUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = (
            'id',
            'name',
            'address',
            'description',
        )
