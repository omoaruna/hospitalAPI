from django.db import models
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from Doctor.models import Doctor
# from django.contrib.auth.models import User
from datetime import date
from django.core.validators import MinValueValidator
# from django.db.models.signals import post_save
# from django.dispatch import receiver
import uuid

GENDER_CHOICES = (
    ("F","Female"),
    ("M","Male")
)
BLOOD_TYPES =(
    ("O+","O+"),
    ("O-","O-"),
    ("A+","A+"),
    ("A-","A-"),
    ("B+","B+"),
    ("B-","B-"),
    ("AB+","AB+"),
    ("AB-","AB-")
)
class Patient(models.Model):
    # user = models.OneToOneField(User,on_delete=models.CASCADE)
    full_name = models.CharField(max_length=300)
    slug = models.SlugField()
    dob = models.DateField(help_text="YYYY-MM-DD")
    # age = models.PositiveIntegerField()
    gender = models.CharField(max_length=20,choices=GENDER_CHOICES)
    height = models.DecimalField(help_text="Enter your height in centimetres",decimal_places=2,max_digits=5,validators=[MinValueValidator(0.01)])
    weight = models.DecimalField(help_text="Enter your weight in kilograms",decimal_places=2,max_digits=5,validators=[MinValueValidator(0.01)])
    known_allergies = models.TextField(blank=True)
    blood_type = models.CharField(max_length=5,choices=BLOOD_TYPES)
    email = models.EmailField()
    phone = PhoneNumberField()
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    @property
    def age(self):
        today = date.today()
        return today.year - self.dob.year

   


    def __str__(self):
        return self.full_name
    
# @receiver(post_save,sender=User)
# def create_patient(sender,instance,created,**kwargs):
#     if created:
#         Patient.objects.create(user=instance)

# @receiver(post_save, sender=User)
# def save_patient(sender,instance,**kwargs):
#     instance.patient.save()
    

    

class Record(models.Model):
    patient = models.ForeignKey(Patient,on_delete=models.CASCADE)
    record_id = models.UUIDField(default=uuid.uuid4,unique=True,editable=False,primary_key=True)
    doctor = models.ForeignKey(Doctor,on_delete=models.CASCADE)
    symptoms = models.TextField()
    diagnosis = models.TextField()
    medication = models.TextField()
    date_updated = models.DateTimeField(auto_now=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.patient.full_name
    
# Create your models here.
