from django.db import models
from django.contrib.auth.models import User
from datetime import date


class AddDonarModle(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    blood_group = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    last_donation = models.DateField()
    address = models.TextField()
    
    def __str__(self):
        return self.name
    
