import django_filters

from hotels.models.rooms import HotelRoom


class HotelRoomFilter(django_filters.FilterSet):
    max_guests = django_filters.NumberFilter(field_name='max_guests',
                                             lookup_expr='gte')
    max_adults = django_filters.NumberFilter(field_name='max_adults',
                                             lookup_expr='gte')
    max_children = django_filters.NumberFilter(field_name='max_children',
                                               lookup_expr='gte')

    class Meta:
        model = HotelRoom
        fields = ('private', 'max_guests', 'max_adults', 'max_children',)
