from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAdminUser

from common.views.mixins import LCRUDViewSet
from reservations.models.reservations import Reservation, ReservationRoom
from reservations.serializers.api.reservation_rooms import \
    ReservationRoomCreateSerializer, ReservationRoomUpdateSerializer, \
    ReservationRoomListSerializer, ReservationRoomRetrieveSerializer
from reservations.serializers.api.reservations import (
    ReservationListSerializer,
    ReservationRetrieveSerializer,
    ReservationCreateSerializer, ReservationUpdateSerializer)


@extend_schema_view(
    retrieve=extend_schema(summary='Деталка бронирования комнаты',
                           tags=['Бронирования комнат']),
    list=extend_schema(summary='Список бронирований комнат',
                       tags=['Бронирования комнат']),
    create=extend_schema(summary='Создать бронирование комнаты',
                         tags=['Бронирования комнат']),
    partial_update=extend_schema(summary='Изменить бронирование '
                                         'комнаты частично',
                                 tags=['Бронирования комнат']),
    destroy=extend_schema(summary='Удалить бронирование комнаты',
                          tags=['Бронирования комнат']),
)
class ReservationRoomView(LCRUDViewSet):
    permission_classes = [IsAdminUser]
    queryset = ReservationRoom.objects.all()
    serializer_class = ReservationRoomListSerializer
    http_method_names = ('get', 'post', 'patch', 'delete',)

    lookup_url_kwarg = 'reservation_room_id'

    multi_serializer_class = {
        'list': ReservationRoomListSerializer,
        'retrieve': ReservationRoomRetrieveSerializer,
        'create': ReservationRoomCreateSerializer,
        'partial_update': ReservationRoomUpdateSerializer,
    }

    def get_queryset(self):
        reservation_id = self.get_value_from_url('id')
        queryset = ReservationRoom.objects.filter(reservation_id=reservation_id)
        return queryset

    def perform_destroy(self, instance):
        if instance.status_id != 'not_checked_in':
            raise ValidationError(f'Нельзя удалить бронирование с '
                                  f'статусом {instance.status}')
        instance.delete()
