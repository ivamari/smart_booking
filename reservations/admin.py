from django.contrib import admin

from reservations.models.reservations import (ReservationClient,
                                              ReservationRoom,
                                              Reservation)


##############################
# INLINES
##############################

class ReservationClientInline(admin.TabularInline):
    model = ReservationClient
    fields = ('client', 'checked', 'is_main_client',)


class ReservationRoomInline(admin.TabularInline):
    model = ReservationRoom
    fields = ('room', 'status',)


##############################
# MODELS
##############################

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('id', 'client', 'status', 'start_date', 'end_date', 'adults',
                    'children')
    list_display_links = ('id', 'client', )

    inlines = (
        ReservationClientInline,
        ReservationRoomInline,
    )
