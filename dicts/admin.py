from django.contrib import admin

from dicts.models.dicts import Gender, AgeType


@admin.register(Gender)
class GenderAdmin(admin.ModelAdmin):
    list_display = ('code', 'name')
    list_display_links = ('code', 'name')


@admin.register(AgeType)
class GenderAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'age_from', 'age_to')
    list_display_links = ('name', )
