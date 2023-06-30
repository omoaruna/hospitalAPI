from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Doctor

class DoctorAdmin(admin.ModelAdmin):
    list_display = ["name","specialty"]
    list_filter = ["specialty"]
    ordering = ["specialty"]

admin.site.register(Doctor,UserAdmin)

# Register your models here.
