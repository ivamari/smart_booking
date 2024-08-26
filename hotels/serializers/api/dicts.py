from common.serializers.mixins import BaseDictMixinSerializer
from hotels.models.dicts import AccommodationType


class AccommodationTypeGetSerializer(BaseDictMixinSerializer):
    class Meta:
        model = AccommodationType
