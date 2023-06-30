from django.contrib import admin


from .models import Appointment
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ["patient","doctor","date_slot","time_slot"]
    list_filter = ["doctor","date_slot","time_slot"]
    ordering = ["date_slot"]

admin.site.register(Appointment,AppointmentAdmin)

# Register your models here.
