from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets

from .serializers import UserSerializer, MeterSerializer, ReadingSerializer, UserMeterSerializer, TestModelSerializer
from .models import User, Meter, Reading, UserMeter, TestModel


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('id')
    serializer_class = UserSerializer

class MeterViewSet(viewsets.ModelViewSet):
    queryset = Meter.objects.all().order_by('id')
    serializer_class = MeterSerializer

class UserMeterViewSet(viewsets.ModelViewSet):
    queryset = UserMeter.objects.all().order_by('id')
    serializer_class = UserMeterSerializer

class ReadingViewSet(viewsets.ModelViewSet):
    queryset = Reading.objects.all().order_by('id')
    serializer_class = ReadingSerializer

class TestModelViewSet(viewsets.ModelViewSet):
    queryset = TestModel.objects.all().order_by('time')
    serializer_class = TestModelSerializer