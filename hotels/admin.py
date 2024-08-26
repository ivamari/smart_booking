from django.contrib import admin

from hotels.models.dicts import AccommodationType
from hotels.models.hotels import Hotel


@admin.register(AccommodationType)
class AccommodationTypeAdmin(admin.ModelAdmin):
    list_display = ('code', 'name')
    list_display_links = ('code', 'name')


@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
