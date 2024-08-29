from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework.permissions import IsAdminUser

from common.views.mixins import LCRUDViewSet
from hotels.models.rooms import Room
from hotels.serializers.api.rooms import (RoomCreateSerializer,
                                          RoomUpdateSerializer,
                                          RoomListSerializer,
                                          RoomRetrieveSerializer)


@extend_schema_view(
    retrieve=extend_schema(summary='Деталка номера отеля',
                           tags=['Номера отеля']),
    list=extend_schema(summary='Список номеров отеля', tags=['Номера отеля']),
    create=extend_schema(summary='Создать номер отеля',
                         tags=['Номера отеля']),
    partial_update=extend_schema(summary='Изменить номер отеля частично',
                                 tags=['Номера отеля']),
    destroy=extend_schema(summary='Удалить номер отеля',
                          tags=['Номера отеля']),
)
class RoomView(LCRUDViewSet):
    queryset = Room.objects.all()
    permission_classes = [IsAdminUser]

    http_method_names = ('get', 'post', 'patch', 'delete',)

    lookup_url_kwarg = 'room_id'

    def get_serializer_class(self):
        if self.action == 'list':
            return RoomListSerializer
        elif self.action == 'retrieve':
            return RoomRetrieveSerializer
        elif self.action == 'create':
            return RoomCreateSerializer
        elif self.action == 'partial_update':
            return RoomUpdateSerializer
        return super().get_serializer_class()

    def get_queryset(self):
        hotel_id = self.kwargs.get('id')
        queryset = Room.objects.filter(hotel_id=hotel_id)
        return queryset

