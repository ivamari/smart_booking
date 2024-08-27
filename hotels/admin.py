from django.contrib import admin
from django.utils.html import format_html

from hotels.models.dicts import AccommodationType
from hotels.models.hotels import Hotel
from hotels.models.rooms import Room


@admin.register(AccommodationType)
class AccommodationTypeAdmin(admin.ModelAdmin):
    list_display = ('code', 'name')
    list_display_links = ('code', 'name')


@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('id', 'number', 'hotel_link', 'accommodation_type_link')
    list_display_links = ('id', 'number')

    def hotel_link(self, obj):
        url = f"/admin/hotels/hotel/{obj.hotel.id}/change/"
        return format_html('<a href="{}">{}</a>', url, obj.hotel)

    hotel_link.short_description = 'Отель'

    def accommodation_type_link(self, obj):
        url = f"/admin/hotels/accommodationtype/{obj.accommodation_type.code}/change/"
        return format_html('<a href="{}">{}</a>', url, obj.accommodation_type)

    accommodation_type_link.short_description = 'Тип размещения'
