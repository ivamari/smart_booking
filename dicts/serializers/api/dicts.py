from rest_framework import serializers

from common.serializers.mixins import BaseDictMixinSerializer
from dicts.models.dicts import Gender, AgeType


class GenderGetSerializer(BaseDictMixinSerializer):
    class Meta:
        model = Gender


class AgeTypeGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = AgeType
        fields = (
            'id',
            'name',
            'age_from',
            'age_to',
        )
