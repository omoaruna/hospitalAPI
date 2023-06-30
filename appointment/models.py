from django.db import models
from django.db import models
from django.db import models
from Patient.models import Patient
from Doctor.models import Doctor
class Appointment(models.Model):
    patient = models.OneToOneField(Patient,on_delete=models.CASCADE)
    doctor = models.OneToOneField(Doctor,on_delete=models.CASCADE)
    date_slot = models.DateField(help_text="YYYY-MM-DD")
    time_slot = models.TimeField(help_text="HH-MM")
    additional_info = models.TextField(blank=True)

    def __str__(self):
        return self.patient.full_name
# Create your models here.
