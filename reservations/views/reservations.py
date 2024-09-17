from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework.permissions import IsAdminUser

from common.views.mixins import LCRUDViewSet
from reservations.models.reservations import Reservation
from reservations.serializers.api.reservations import ReservationListSerializer


@extend_schema_view(
    # retrieve=extend_schema(summary='Деталка отеля',
    #                        tags=['Отели']),
    list=extend_schema(summary='Список бронирований', tags=['Бронирования']),
    # create=extend_schema(summary='Создать отель',
    #                      tags=['Отели']),
    # partial_update=extend_schema(summary='Изменить отель частично',
    #                              tags=['Отели']),
    # destroy=extend_schema(summary='Удалить отель',
    #                       tags=['Отели']),
)
class ReservationView(LCRUDViewSet):
    permission_classes = [IsAdminUser]
    queryset = Reservation.objects.all()
    serializer_class = ReservationListSerializer
    http_method_names = ('get', 'post', 'patch', 'delete',)

    multi_serializer_class = {
        'list': ReservationListSerializer,
        # 'retrieve': HotelRetrieveSerializer,
        # 'create': HotelCreateSerializer,
        # 'partial_update': HotelUpdateSerializer,
    }
