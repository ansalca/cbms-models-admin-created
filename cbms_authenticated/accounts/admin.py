from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, Staff, Student, Parent, Bus, Driver, IncidentReport

# Custom User admin
class UserAdmin(BaseUserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email', 'contact_number')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
        ('Role', {'fields': ('role',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'role'),
        }),
    )
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'role')
    search_fields = ('username', 'first_name', 'last_name', 'email')
    ordering = ('username',)

# Custom Staff admin
class StaffAdmin(admin.ModelAdmin):
    list_display = ('user', 'position', 'bus')
    search_fields = ('user__username', 'position', 'bus__plate_number')
    list_filter = ('position',)

# Custom Student admin
class StudentAdmin(admin.ModelAdmin):
    list_display = ('user', 'department', 'year', 'bus_fare_amount', 'payment_status', 'parent', 'bus')
    search_fields = ('user__username', 'department', 'parent__user__username', 'bus__plate_number')
    list_filter = ('department', 'year', 'payment_status')

# Custom Parent admin
class ParentAdmin(admin.ModelAdmin):
    list_display = ('user',)
    search_fields = ('user__username',)

# Custom Bus admin
class BusAdmin(admin.ModelAdmin):
    list_display = ('plate_number', 'capacity', 'current_location', 'driver')
    search_fields = ('plate_number', 'driver__user__username')
    list_filter = ('capacity',)

# Custom Driver admin
class DriverAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone', 'license_number')
    search_fields = ('user__username', 'phone', 'license_number')

# Custom Incident Report admin
class IncidentReportAdmin(admin.ModelAdmin):
    list_display = ('user', 'bus', 'description', 'timestamp', 'location')
    search_fields = ('user__username', 'bus__plate_number', 'location')
    list_filter = ('timestamp', 'location')

# Register all models with their custom admin configurations
admin.site.register(User, UserAdmin)
admin.site.register(Staff, StaffAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Parent, ParentAdmin)
admin.site.register(Bus, BusAdmin)
admin.site.register(Driver, DriverAdmin)
admin.site.register(IncidentReport, IncidentReportAdmin)