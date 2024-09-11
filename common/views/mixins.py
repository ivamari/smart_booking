from django.shortcuts import get_object_or_404
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet


class ContextDataMixinView:
    def get_value_from_url(self, value):
        return self.kwargs.get(value)

    def get_object_from_model(self, key, model, field, raise_not_found=False):
        lookup = {field: key}

        if raise_not_found:
            return get_object_or_404(model, **lookup)
        else:
            return model.objects.filter(**lookup).first()


class ExtendedView(ContextDataMixinView):
    multi_serializer_class = {}

    def get_serializer_class(self):
        try:
            return self.multi_serializer_class[self.action]
        except KeyError:
            return super().get_serializer_class()


class LCRUDViewSet(ExtendedView,
                   GenericViewSet,
                   mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.ListModelMixin,
                   mixins.DestroyModelMixin):
    pass
