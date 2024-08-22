from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet


class LCRUDViewSet(GenericViewSet,
                   mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.ListModelMixin,
                   mixins.DestroyModelMixin):
    pass
