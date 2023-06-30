from django.shortcuts import render
from .serializers import PatientSerializer
from .models import Patient
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.decorators import permission_classes,api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import GenericAPIView

class PatientRegistration(GenericAPIView):
    def post(self,request):
        # request.method == "POST"
        serializer = PatientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"Successful Registration"},serializer.data,status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
class PatientList(GenericAPIView):
    def get(self,request):
        # request.method == "GET"
        all_patients = Patient.objects.all()
        serializer = PatientSerializer(all_patients,many = True)
        return Response(data=serializer.data,status=status.HTTP_200_OK)
    
class PatientDetails(GenericAPIView):
    def get(self,request,slug):
        # request.method == "GET"
        single_patient = Patient.objects.get(slug=slug)
        serializer = PatientSerializer(single_patient)
        return Response(data=serializer.data,status=status.HTTP_200_OK)
    
# @api_view(["GET"])
# @permission_classes([IsAuthenticated])
# def search_patients(request,slug):   
#     staff_user = request.user
#     if staff_user.is_staff:
#         # query = request.GET.get("query","")
#         patients = Patient.objects.filter(slug=slug)

#         serializer = PatientSerializer(patients,many=True)
#         return Response(data=serializer.data)
#     return Response({"message":"You are not authorized to access this endpoint"},status=status.HTTP_403_FORBIDDEN)


# Create your views here.
