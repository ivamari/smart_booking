from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework.permissions import IsAdminUser

from common.views.mixins import LCRUDViewSet
from hotels.models.rooms import HotelRoom
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
class HotelRoomView(LCRUDViewSet):
    queryset = HotelRoom.objects.all()
    permission_classes = [IsAdminUser]
    serializer_class = RoomListSerializer

    http_method_names = ('get', 'post', 'patch', 'delete',)

    lookup_url_kwarg = 'room_id'

    multi_serializer_class = {
        'list': RoomListSerializer,
        'retrieve': RoomRetrieveSerializer,
        'create': RoomCreateSerializer,
        'partial_update': RoomUpdateSerializer,
    }

    def get_queryset(self):
        hotel_id = self.kwargs.get('id')
        queryset = HotelRoom.objects.filter(hotel_id=hotel_id)
        return queryset
