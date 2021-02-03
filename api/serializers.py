# serializers.py

from rest_framework import serializers
from .models import User, Meter, Reading, UserMeter, TestModel

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id','name','sname','email')

class MeterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Meter
        fields = ('id','name','location')

class ReadingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Reading
        fields = ('id','meter','value','time','date')

class UserMeterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserMeter
        fields = ('id','user','meter')

class TestModelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TestModel
        fields = ('device','time','data','seqNumber')


