from django.contrib import admin
from django.utils.html import format_html

from common.admin import InfoModelAdmin
from hotels.models.dicts import AccommodationType, RoomStatus
from hotels.models.hotels import Hotel, HotelPolicy
from hotels.models.rooms import HotelRoom, HotelRoomSettings, HotelRoomStatus


##############################
# INLINES
##############################

class HotelRoomStatusInline(admin.TabularInline):
    model = HotelRoomStatus
    fields = ('status',)
    autocomplete_fields = ('status', )


class HotelRoomSettingsInline(admin.StackedInline):
    model = HotelRoomSettings
    fields = ('has_airconditioner', 'has_tv', 'has_wifi')


class HotelPolicyInline(admin.StackedInline):
    model = HotelPolicy
    fields = ('check_in', 'check_out')


##############################
# MODELS
##############################


@admin.register(HotelRoomSettings)
class RoomSettingsAdmin(admin.ModelAdmin):
    list_display = ('room', 'has_airconditioner', 'has_tv', 'has_wifi')
    list_display_links = ('room',)
    autocomplete_fields = ('room',)


@admin.register(HotelRoomStatus)
class HotelRoomStatusAdmin(InfoModelAdmin):
    list_display = ('room', 'status')
    list_display_links = ('room',)
    search_fields = ('status', )


@admin.register(AccommodationType)
class AccommodationTypeAdmin(admin.ModelAdmin):
    list_display = ('code', 'name')
    list_display_links = ('code', 'name')
    search_fields = ('code', 'name', )


@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'id',)
    inlines = (
        HotelPolicyInline,
    )


@admin.register(RoomStatus)
class RoomStatusAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'color', 'sort')
    list_display_links = ('code', 'name')
    search_fields = ('code', 'name', )


@admin.register(HotelRoom)
class HotelRoomAdmin(admin.ModelAdmin):
    list_display = ('id', 'number', 'hotel_link', 'accommodation_type_link')
    list_display_links = ('id', 'number')
    search_fields = ('id', 'number', )
    autocomplete_fields = ('hotel', 'accommodation_type', )
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
