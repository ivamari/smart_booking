from django.shortcuts import get_object_or_404
from rest_framework import serializers


class BaseDictMixinSerializer(serializers.Serializer):
    code = serializers.CharField()
    name = serializers.CharField()


class ContextDataMixin:
    def get_value_from_url(self, value):
        return self.context['view'].kwargs.get(value)

    def get_object_from_model(self, key, model, field, raise_not_found=False):
        lookup = {field: key}

        if raise_not_found:
            return get_object_or_404(model, **lookup)
        else:
            return model.objects.filter(**lookup).first()


class ExtendedModelSerializer(ContextDataMixin, serializers.ModelSerializer):
    pass
