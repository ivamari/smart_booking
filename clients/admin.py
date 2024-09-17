from django.contrib import admin

from clients.models.clients import Client


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name')
    list_display_links = ('id', 'full_name')
    autocomplete_fields = ('gender', )
    search_fields = ('id', 'first_name', 'last_name', )
