from django.shortcuts import get_object_or_404
from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response

from common.views.mixins import LCRUDViewSet
from hotels.models.rooms import Room
from hotels.serializers.api.rooms import (RoomGetSerializer,
                                          RoomCreateSerializer,
                                          RoomUpdateSerializer)


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
    serializer_class = RoomGetSerializer

    http_method_names = ('get', 'post', 'patch', 'delete',)

    lookup_url_kwarg = 'room_id'

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve':
            return RoomGetSerializer
        elif self.action == 'create':
            return RoomCreateSerializer
        elif self.action == 'partial_update':
            return RoomUpdateSerializer
        return super().get_serializer_class()

    def get_object(self):
        hotel_id = self.kwargs.get('id')
        rooms_id = self.kwargs.get('room_id')
        return get_object_or_404(Room, id=rooms_id, hotel_id=hotel_id)

    def get_queryset(self):
        hotel_id = self.kwargs.get('id')
        queryset = Room.objects.all().filter(hotel_id=hotel_id)
        return queryset

    def retrieve(self, request, *args, **kwargs):
        room = self.get_object()
        serializer = self.get_serializer(room)
        return Response(serializer.data)

    def perform_create(self, serializer):
        hotel_id = self.kwargs.get('id')
        serializer.save(hotel_id=hotel_id)

    def perform_update(self, serializer):
        hotel_id = self.kwargs.get('id')
        serializer.save(hotel_id=hotel_id)
