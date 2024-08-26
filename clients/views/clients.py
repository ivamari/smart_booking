from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework.permissions import IsAdminUser

from clients.models.clients import Client
from clients.serializers.api.clients import (ClientGetSerializer,
                                             ClientCreateSerializer,
                                             ClientUpdateSerializer)
from common.views.mixins import LCRUDViewSet


@extend_schema_view(
    retrieve=extend_schema(summary='Деталка клиента',
                           tags=['Клиенты']),
    list=extend_schema(summary='Список клиентов', tags=['Клиенты']),
    create=extend_schema(summary='Создать клиента',
                         tags=['Клиенты']),
    partial_update=extend_schema(summary='Изменить клиента частично',
                                 tags=['Клиенты']),
    destroy=extend_schema(summary='Удалить клиента',
                          tags=['Клиенты']),
)
class ClientView(LCRUDViewSet):
    permission_classes = [IsAdminUser]
    queryset = Client.objects.all()
    http_method_names = ('get', 'post', 'patch', 'delete',)

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve':
            return ClientGetSerializer
        elif self.action == 'create':
            return ClientCreateSerializer
        elif self.action == 'partial_update':
            return ClientUpdateSerializer
        return super().get_serializer_class()
