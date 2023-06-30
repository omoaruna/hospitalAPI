from django.urls import path
from .views import *
urlpatterns = [
    path("search_patient/<slug:slug>/",search_patient,name= "patient_search")
]
