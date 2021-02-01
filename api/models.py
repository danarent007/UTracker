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

    def __str__(self):
        return self.name
    