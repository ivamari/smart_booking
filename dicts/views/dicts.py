from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from dicts.models.dicts import Gender, AgeType
from dicts.serializers.api.dicts import (GenderGetSerializer,
                                         AgeTypeGetSerializer)


@extend_schema_view(
    get=extend_schema(summary='Список гендеров', tags=['Словари'])
)
class GendersView(ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Gender.objects.all()
    serializer_class = GenderGetSerializer


@extend_schema_view(
    get=extend_schema(summary='Диапазоны возрастов', tags=['Словари'])
)
class AgeTypeView(ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = AgeType.objects.all()
    serializer_class = AgeTypeGetSerializer
