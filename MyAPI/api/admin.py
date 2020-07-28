from django.contrib import admin
from api.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from api.forms import UserAdminChangeForm, UserAdminCreationForm


class UserAdmin(BaseUserAdmin):
	# The forms to add and change user instances
	form = UserAdminChangeForm
	add_form = UserAdminCreationForm
	# The fields to be used in displaying the User model.
	# These override the definitions on the base UserAdmin
	# that reference specific fields on auth.User.
	list_display = ('username', 'request_limits_developer', 'request_limits_organization')
	list_filter = ('username',)
	fieldsets = (
		(None, {'fields': ('username', 'email', 'password', 'request_limits_developer', 'request_limits_organization')}),
		('Personal info', {'fields': ()}),
		('Permissions', {'fields': ()}),
	)
	search_fields = ('username',)
	ordering = ('username',)
	filter_horizontal = ()


# Register your models here.
admin.site.register(User, UserAdmin)
# admin.site.register(User)
