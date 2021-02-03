from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=60)
    sname = models.CharField(max_length=60)
    email = models.CharField(max_length=60)

    def __str__(self):
        return self.name

class Meter(models.Model):
    name = models.CharField(max_length=30)
    location = models.CharField(max_length=100)
    owner = models.CharField(max_length=60)

    def __str__(self):
        return self.name
    
class Reading(models.Model):
    meter = models.ForeignKey(Meter, on_delete=models.CASCADE)
    value = models.FloatField()
    time = models.TimeField()
    date = models.DateField()

    def __str__(self):
        return self.id


class UserMeter(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    meter = models.ForeignKey(Meter, on_delete=models.CASCADE)

    def __str__(self):
        return self.user

class TestModel(models.Model):
    device = models.CharField(max_length=60)
    time = models.CharField(max_length=60)
    data = models.CharField(max_length=60)
    seqNumber = models.CharField(max_length=60)

    def __str__(self):
        return self.id
    