from django.contrib import admin
from django.contrib import admin
from django.contrib import admin
from .models import *
class PatientAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug":("full_name",)}
    list_filter = ["gender"]
    ordering = ["full_name"]
    list_display = ["id","full_name","gender"]
admin.site.register(Patient,PatientAdmin)
    
class RecordAdmin(admin.ModelAdmin):
    list_display = ["patient","record_id"]
    ordering = ["patient"]

admin.site.register(Record,RecordAdmin)
# Register your models here.
