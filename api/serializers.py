# serializers.py

from rest_framework import serializers
from .models import User, Meter

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id','name','sname','email')

class MeterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Meter
        fields = ('id','name','location')