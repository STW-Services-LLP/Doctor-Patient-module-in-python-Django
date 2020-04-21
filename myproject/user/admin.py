from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

# Register your models here.

class CustomUserAdmin(UserAdmin):
	list_display = ('username','email','last_login','is_staff','is_doctor','is_patient')
	search_fields = ('email' , 'username')
	# readonly_fields = ('last_login')

	filter_horizontal = ()
	list_filter = ()
	fieldsets = ()



admin.site.register(CustomUser , CustomUserAdmin)