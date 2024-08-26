from django.contrib import admin

from clients.models.clients import Client


@admin.register(Client)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name')
    list_display_links = ('id', 'full_name')