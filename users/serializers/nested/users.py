from rest_framework import serializers

from users.models.users import User


class UserHotelRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'full_name',
        )
