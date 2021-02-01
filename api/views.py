from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets

from .serializers import UserSerializer, MeterSerializer
from .models import User, Meter


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('id')
    serializer_class = UserSerializer

class MeterViewSet(viewsets.ModelViewSet):
    queryset = Meter.objects.all().order_by('id')
    serializer_class = MeterSerializer