from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from common.serializers.mixins import BaseDictMixinSerializer
from hotels.models.dicts import AccommodationType


class AccommodationTypeGetSerializer(BaseDictMixinSerializer):
    class Meta:
        model = AccommodationType


class AccommodationTypeSearchSerializer(BaseDictMixinSerializer):
    class Meta:
        model = AccommodationType


class AccommodationTypeListSerializer(serializers.ModelSerializer):
    rooms_total = serializers.IntegerField()

    class Meta:
        model = AccommodationType
        fields = (
            'code',
            'name',
            'description',
            'max_guests',
            'max_adults',
            'max_children',
            'rooms_total'
        )


class AccommodationTypeRetrieveSerializer(serializers.ModelSerializer):
    rooms_total = serializers.IntegerField()

    class Meta:
        model = AccommodationType
        fields = (
            'code',
            'name',
            'description',
            'max_guests',
            'max_adults',
            'max_children',
            'rooms_total'
        )


class AccommodationTypeCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccommodationType
        fields = (
            'code',
            'name',
            'description',
            'private',
            'max_guests',
            'max_adults',
            'max_children',
        )


class AccommodationTypeUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccommodationType
        fields = (
            'name',
            'description',
            'private',
            'max_guests',
            'max_adults',
            'max_children',
        )


class AccommodationTypeDeleteSerializer(serializers.ModelSerializer):
    rooms_total = serializers.IntegerField()

    class Meta:
        model = AccommodationType
        fields = (
            'code',
            'name',
            'description',
            'max_guests',
            'max_adults',
            'max_children',
            'rooms_total'
        )

    def validate_delete(self, instance):
        if instance.rooms_total > 0:
            raise ValidationError('Нельзя удалить тип размещения, '
                                  'у которого есть связанные комнаты.')
        return instance
