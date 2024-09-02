from rest_framework import serializers


class BaseDictMixinSerializer(serializers.Serializer):
    code = serializers.CharField()
    name = serializers.CharField()
