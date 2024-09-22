from django.contrib import admin

from common.admin import InfoModelAdmin
from reservations.models.dicts import ReservationStatus, ReservationRoomStatus
from reservations.models.reservations import (ReservationClient,
                                              ReservationRoom,
                                              Reservation)


##############################
# INLINES
##############################

class ReservationClientInline(admin.TabularInline):
    model = ReservationClient
    fields = ('client', 'checked', 'is_main_client',)
    autocomplete_fields = ('client',)


class ReservationRoomInline(admin.TabularInline):
    model = ReservationRoom
    fields = ('room', 'status',)
    autocomplete_fields = ('room', 'status',)


##############################
# MODELS
##############################

@admin.register(ReservationStatus)
class ReservationStatusAdmin(admin.ModelAdmin):
    search_fields = ('name', 'code',)


@admin.register(ReservationRoom)
class ReservationRoomAdmin(admin.ModelAdmin):
    list_display = ('id', 'reservation', 'room', 'status', )
    list_display_links = ('id', 'reservation', )
    search_fields = ('room', 'status',)


@admin.register(ReservationClient)
class ReservationClientAdmin(admin.ModelAdmin):
    search_fields = ('client',)


@admin.register(ReservationRoomStatus)
class ReservationRoomStatusAdmin(admin.ModelAdmin):
    search_fields = ('code', 'name',)


@admin.register(Reservation)
class ReservationAdmin(InfoModelAdmin):
    list_display = ('id', 'client', 'status', 'start_date', 'end_date',
                    'adults', 'children')
    list_display_links = ('id', 'client',)
    autocomplete_fields = ('status', 'client')

    inlines = (
        ReservationClientInline,
        ReservationRoomInline,
    )
