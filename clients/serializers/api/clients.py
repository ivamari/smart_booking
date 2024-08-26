from rest_framework import serializers

from clients.models.clients import Client
from common.validators import validate_dob
from dicts.models.dicts import Gender
from dicts.serializers.api.dicts import GenderGetSerializer


class ClientGetSerializer(serializers.ModelSerializer):
    gender = GenderGetSerializer()

    class Meta:
        model = Client
        fields = (
            'id',
            'full_name',
            'dob',
            'email',
            'phone',
            'gender',
        )


class ClientCreateSerializer(serializers.ModelSerializer):
    gender = serializers.PrimaryKeyRelatedField(
        queryset=Gender.objects.all()
    )

    class Meta:
        model = Client
        fields = (
            'first_name',
            'last_name',
            'middle_name',
            'dob',
            'email',
            'phone',
            'gender',
        )

    def validate_dob(self, value):
        return validate_dob(value)


class ClientUpdateSerializer(serializers.ModelSerializer):
    gender = serializers.PrimaryKeyRelatedField(queryset=Gender.objects.all())

    class Meta:
        model = Client
        fields = (
            'first_name',
            'last_name',
            'middle_name',
            'dob',
            'email',
            'phone',
            'gender',
        )

    def validate_dob(self, value):
        return validate_dob(value)
