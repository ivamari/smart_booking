from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAdminUser

from common.views.mixins import LCRUDViewSet
from reservations.models.reservations import ReservationRoom, ReservationClient
from reservations.serializers.api.clients import (
    ReservationClientListSerializer, ReservationClientRetrieveSerializer,
    ReservationClientCreateSerializer, ReservationClientUpdateSerializer)


@extend_schema_view(
    retrieve=extend_schema(summary='Деталка бронирования клиента',
                           tags=['Бронирования клиентов']),
    list=extend_schema(summary='Список бронирований клиентов',
                       tags=['Бронирования клиентов']),
    create=extend_schema(summary='Создать бронирование клиента',
                         tags=['Бронирования клиентов']),
    partial_update=extend_schema(summary='Изменить бронирование '
                                         'клиента частично',
                                 tags=['Бронирования клиентов']),
    destroy=extend_schema(summary='Удалить бронирование клиента',
                          tags=['Бронирования клиентов']),
)
class ReservationClientView(LCRUDViewSet):
    permission_classes = [IsAdminUser]
    queryset = ReservationRoom.objects.all()
    serializer_class = ReservationClientListSerializer
    http_method_names = ('get', 'post', 'patch', 'delete',)

    lookup_url_kwarg = 'reservation_client_id'

    multi_serializer_class = {
        'list': ReservationClientListSerializer,
        'retrieve': ReservationClientRetrieveSerializer,
        'create': ReservationClientCreateSerializer,
        'partial_update': ReservationClientUpdateSerializer,
    }

    def get_queryset(self):
        reservation_id = self.get_value_from_url('id')
        queryset = ReservationClient.objects.filter(
            reservation_id=reservation_id)
        return queryset

    def perform_destroy(self, instance):
        if instance.is_main_client:
            raise ValidationError(f'Нельзя удалить бронирование '
                                  f'главного клиента.')
        instance.delete()
