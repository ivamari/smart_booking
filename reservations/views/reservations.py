from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAdminUser

from common.views.mixins import LCRUDViewSet
from reservations.models.reservations import Reservation
from reservations.serializers.api.reservations import (
    ReservationListSerializer,
    ReservationRetrieveSerializer,
    ReservationCreateSerializer, ReservationUpdateSerializer)


@extend_schema_view(
    retrieve=extend_schema(summary='Список бронирований',
                           tags=['Бронирования']),
    list=extend_schema(summary='Список бронирований', tags=['Бронирования']),
    create=extend_schema(summary='Создать бронирование',
                         tags=['Бронирования']),
    partial_update=extend_schema(summary='Изменить бронирование частично',
                                 tags=['Бронирования']),
    destroy=extend_schema(summary='Удалить бронирование',
                          tags=['Бронирования']),
)
class ReservationView(LCRUDViewSet):
    permission_classes = [IsAdminUser]
    queryset = Reservation.objects.all()
    serializer_class = ReservationListSerializer
    http_method_names = ('get', 'post', 'patch', 'delete',)

    multi_serializer_class = {
        'list': ReservationListSerializer,
        'retrieve': ReservationRetrieveSerializer,
        'create': ReservationCreateSerializer,
        'partial_update': ReservationUpdateSerializer,
    }

    def perform_destroy(self, instance):
        if instance.status != 'not_confirmed':
            raise ValidationError(f'Нельзя удалить бронирование с '
                                  f'статусом {instance.status}')
        instance.delete()
