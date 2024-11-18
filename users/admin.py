from django.contrib import admin
from django.contrib.auth.models import User as BaseUser, Group as BaseGroup

from users.models.users import User
from users.models.groups import Group


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'email', )
    list_display_links = ('id', 'full_name')
    filter_horizontal = ('groups', 'user_permissions',)


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')


try:
    admin.site.unregister(BaseUser)
except admin.sites.NotRegistered:
    pass

try:
    admin.site.unregister(BaseGroup)
except admin.sites.NotRegistered:
    pass
