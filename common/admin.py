from django.contrib import admin


class DateModelAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')


class InfoModelAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at', 'created_by', 'updated_by')
