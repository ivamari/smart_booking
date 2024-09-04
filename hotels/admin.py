from django.contrib import admin
from django.utils.html import format_html

from hotels.models.dicts import AccommodationType, RoomStatus
from hotels.models.hotels import Hotel
from hotels.models.rooms import HotelRoom, HotelRoomSettings, HotelRoomStatus


##############################
# INLINES
##############################

class HotelRoomStatusInline(admin.TabularInline):
    model = HotelRoomStatus
    fields = ('status',)


class HotelRoomSettingsInline(admin.StackedInline):
    model = HotelRoomSettings
    fields = ('has_airconditioner', 'has_tv', 'has_wifi')


##############################
# MODELS
##############################

@admin.register(HotelRoomSettings)
class RoomSettingsAdmin(admin.ModelAdmin):
    list_display = ('room', 'has_airconditioner', 'has_tv', 'has_wifi')
    list_display_links = ('room',)


@admin.register(HotelRoomStatus)
class HotelRoomStatusAdmin(admin.ModelAdmin):
    list_display = ('room', 'status')
    list_display_links = ('room',)


@admin.register(AccommodationType)
class AccommodationTypeAdmin(admin.ModelAdmin):
    list_display = ('code', 'name')
    list_display_links = ('code', 'name')


@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')


@admin.register(RoomStatus)
class RoomStatusAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'color', 'sort')
    list_display_links = ('code', 'name')


@admin.register(HotelRoom)
class HotelRoomAdmin(admin.ModelAdmin):
    list_display = ('id', 'number', 'hotel_link', 'accommodation_type_link')
    list_display_links = ('id', 'number')

    inlines = (
        HotelRoomStatusInline,
        HotelRoomSettingsInline,
    )

    def hotel_link(self, obj):
        url = f"/admin/hotels/hotel/{obj.hotel.id}/change/"
        return format_html('<a href="{}">{}</a>', url, obj.hotel)

    hotel_link.short_description = 'Отель'

    def accommodation_type_link(self, obj):
        url = f"/admin/hotels/accommodationtype/{obj.accommodation_type.code}/change/"
        return format_html('<a href="{}">{}</a>', url, obj.accommodation_type)

    accommodation_type_link.short_description = 'Тип размещения'
