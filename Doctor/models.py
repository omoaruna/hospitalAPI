from django.db import models
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import AbstractUser, Group
from django.db.models.signals import post_save
from django.dispatch import receiver
SPECIALTY = (
    ("PED","Pediatrician"),
    ("OBGYN","Gynecologist"),
    ("FAM","Family Physician"),
    ("DERM","Dermatologist"),
    ("RAD", "Radiologist"),
    ("PSY","Psychiatrist"),
    ("CAD","Cardiologist")
)

class Doctor(AbstractUser):
    is_staff = models.BooleanField(default=True)
    # user = models.OneToOneField(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    # username = models.CharField(max_length=300,default="",unique=True)
    # password = models.CharField(max_length=250,default="FR33DOMLIB3RTY")
    specialty = models.CharField(max_length=250,choices=SPECIALTY)
    phone = PhoneNumberField()
    date_added = models.DateTimeField(auto_now=True)
    email = models.EmailField(verbose_name="email")

    # @property
    # def email(self):
    #     return f"dr{self.name.lower().strip()}@myhospital.com"
    
    def __str__(self):
        return self.username
    
# @receiver(post_save,sender=Doctor)

# Create your models here.
