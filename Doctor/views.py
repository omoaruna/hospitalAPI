from django.shortcuts import render

from Patient.serializers import PatientSerializer
from Patient.models import Patient
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.decorators import permission_classes,api_view
from rest_framework.permissions import IsAuthenticated

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def search_patient(request,slug):   
    staff_user = request.user
    if staff_user.is_staff:
        # query = request.GET.get("query","")
        patient = Patient.objects.filter(slug=slug)

        serializer = PatientSerializer(patient)
        return Response(data=serializer.data)
    return Response({"message":"You are not authorized to access this endpoint"},status=status.HTTP_403_FORBIDDEN)

# Create your views here.
