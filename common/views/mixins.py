from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet


class ExtendedView:
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
