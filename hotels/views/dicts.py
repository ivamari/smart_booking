from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from hotels.models.dicts import AccommodationType
from hotels.serializers.api.dicts import AccommodationTypeGetSerializer


@extend_schema_view(
    get=extend_schema(summary='Список типов размещений', tags=['Словари'])
)
class AccommodationTypeView(ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = AccommodationType.objects.all()
    serializer_class = AccommodationTypeGetSerializer
