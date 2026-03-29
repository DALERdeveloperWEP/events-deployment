from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework_simplejwt.authentication import JWTAuthentication

from apps.registrations.models import Registration
from apps.registrations.serializers import RegistrationSerializer

class RegistrationViewSet(viewsets.ModelViewSet):
    
    permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes = [JWTAuthentication] 
    
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer
    