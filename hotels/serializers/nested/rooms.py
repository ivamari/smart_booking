from rest_framework import serializers

from hotels.models.rooms import HotelRoomSettings, HotelRoomStatus


class HotelRoomSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelRoomSettings
        fields = (
            'has_airconditioner',
            'has_tv',
            'has_wifi',
        )


class HotelRoomStatusSerializer(serializers.ModelSerializer):
    status = serializers.SerializerMethodField()
    updated_by = serializers.SerializerMethodField()

    class Meta:
        model = HotelRoomStatus
        fields = (
            'status',
            'updated_at',
            'updated_by'
        )

    def get_status(self, obj):
        return {
            "code": obj.status.code,
            "name": obj.status.name,
            "color": obj.status.color,
        }

    def get_updated_by(self, obj):
        user = obj.updated_by
        if user:
            return {
                "id": user.id,
                "full_name": user.full_name
            }
        return None
