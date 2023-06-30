from django.urls import path
from .views import *
urlpatterns = [
    path("register/",PatientRegistration.as_view(),name="register"),
    path("all_patients/",PatientList.as_view(),name="all_patients"),
    path("<str:slug>/",PatientDetails.as_view(),name = "patient_details"),
    # path("search/<str:slug>/=",search_patients,name="patients_search")
]