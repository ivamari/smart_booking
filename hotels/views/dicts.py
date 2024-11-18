from django.db.models import Count
from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from common.views.mixins import LCRUDViewSet
from hotels.models.dicts import AccommodationType
from hotels.serializers.api.dicts import (AccommodationTypeListSerializer,
                                          AccommodationTypeRetrieveSerializer,
                                          AccommodationTypeCreateSerializer,
                                          AccommodationTypeUpdateSerializer,
                                          AccommodationTypeDeleteSerializer,
                                          AccommodationTypeSearchSerializer)

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter


@extend_schema_view(
    get=extend_schema(summary='Список типов размещений Search',
                      tags=['Словари']),
)
class AccommodationTypeSearchView(ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = AccommodationType.objects.all()
    serializer_class = AccommodationTypeSearchSerializer

    filter_backends = (
        SearchFilter,
        DjangoFilterBackend,
    )

    search_fields = ('code', 'name', 'description',)
    filterset_fields = ('private',)

    def get_queryset(self):
        queryset = AccommodationType.objects.filter(private=False)
        return queryset


@extend_schema_view(
    retrieve=extend_schema(summary='Деталка типа размещения',
                           tags=['Типы размещений']),
    list=extend_schema(summary='Список типов размещений',
                       tags=['Типы размещений']),
    create=extend_schema(summary='Создать тип размещения',
                         tags=['Типы размещений']),
    partial_update=extend_schema(summary='Изменить тип размещения частично',
                                 tags=['Типы размещений']),
    destroy=extend_schema(summary='Удалить тип размещения',
                          tags=['Типы размещений']),
)
class AccommodationTypeHotelsView(LCRUDViewSet):
    permission_classes = [IsAuthenticated]
    queryset = AccommodationType.objects.all()
    serializer_class = AccommodationTypeListSerializer
    http_method_names = ('get', 'post', 'patch', 'delete',)

    multi_serializer_class = {
        'list': AccommodationTypeListSerializer,
        'retrieve': AccommodationTypeRetrieveSerializer,
        'create': AccommodationTypeCreateSerializer,
        'partial_update': AccommodationTypeUpdateSerializer,
        'destroy': AccommodationTypeDeleteSerializer,
    }

    filter_backends = (
        SearchFilter,
        DjangoFilterBackend,
    )

    search_fields = ('code', 'name', 'description',)
    filterset_fields = ('private',)

    def get_queryset(self):
        queryset = AccommodationType.objects.annotate(
            rooms_total=Count('rooms'))
        return queryset

    def perform_destroy(self, instance):
        serializer = self.get_serializer(instance)
        serializer.validate_delete(instance)
        instance.delete()
