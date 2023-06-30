from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from django.conf import settings
SPECIALTY = (
    ("PED","Pediatrician"),
    ("OBGYN","Gynecologist"),
    ("FAM","Family Physician"),
    ("DERM","Dermatologist"),
    ("RAD", "Radiologist"),
    ("PSY","Psychiatrist"),
    ("CAD","Cardiologist")
)

class Doctor(models.Model):
    is_staff = models.BooleanField(default=True)
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    # username = models.CharField(max_length=300,default="",unique=True)
    # password = models.CharField(max_length=250,default="FR33DOMLIB3RTY")
    specialty = models.CharField(max_length=250,choices=SPECIALTY)
    phone = PhoneNumberField()
    date_added = models.DateTimeField(auto_now=True)
# Create your models here.
