from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models

UserAdmin.fieldsets[2][1]['fields'] = (
    'is_active', 'is_staff', 'is_author', 'is_superuser', 'special_user', 'groups', 'user_permissions'
)

UserAdmin.list_display += ('is_author', 'is_special_user')
admin.site.register(models.User,UserAdmin)