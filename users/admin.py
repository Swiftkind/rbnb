from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import ugettext_lazy as _

from users.models import User


class UserAdmin(BaseUserAdmin):
    """ Modified the UserAdmin to remove the username field. 
    """

    ordering = ('email',)

    list_display = ('email', 'is_staff',)
    list_filter = ('is_staff',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'is_host')}),
        (_('Important dates'), {'fields': ('date_of_birth',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'date_of_birth',),
            }),
    )

admin.site.register(User, UserAdmin)