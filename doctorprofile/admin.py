from django.contrib import admin
from .models import *

class DoctorAdmin(admin.ModelAdmin):
    list_display = ["name","specialty"]
    list_filter = ["specialty"]

admin.site.register(Doctor,DoctorAdmin)


# Register your models here.
