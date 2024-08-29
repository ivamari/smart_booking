from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework.permissions import IsAdminUser

from common.views.mixins import LCRUDViewSet
from hotels.models.hotels import Hotel
from hotels.serializers.api.hotels import (HotelCreateSerializer,
                                           HotelUpdateSerializer,
                                           HotelListSerializer,
                                           HotelRetrieveSerializer)


@extend_schema_view(
    retrieve=extend_schema(summary='Деталка отеля',
                           tags=['Отели']),
    list=extend_schema(summary='Список отелей', tags=['Отели']),
    create=extend_schema(summary='Создать отель',
                         tags=['Отели']),
    partial_update=extend_schema(summary='Изменить отель частично',
                                 tags=['Отели']),
    destroy=extend_schema(summary='Удалить отель',
                          tags=['Отели']),
)
class HotelView(LCRUDViewSet):
    permission_classes = [IsAdminUser]
    queryset = Hotel.objects.all()
    http_method_names = ('get', 'post', 'patch', 'delete',)

    def get_serializer_class(self):
        if self.action == 'list':
            return HotelListSerializer
        elif self.action == 'retrieve':
            return HotelRetrieveSerializer
        elif self.action == 'create':
            return HotelCreateSerializer
        elif self.action == 'partial_update':
            return HotelUpdateSerializer
        return super().get_serializer_class()
