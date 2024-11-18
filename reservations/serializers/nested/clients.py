from rest_framework import serializers

from clients.models.clients import Client


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = (
            'id',
            'full_name',
            'phone',
            'dob',
        )
