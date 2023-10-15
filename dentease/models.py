from django.db import models
from django.contrib.auth.models import User

class Denstist(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    registration_number = models.CharField(max_length=50)
    email = models.EmailField(max_length=150)
    clinicAddress = models.CharField(max_length=100, default="")
    contact = models.CharField(default="",max_length=10)
    description = models.CharField(max_length=500, default="Edit Profile to add description")
    location = models.CharField(max_length=100, default="Edit profile to add location")


    def __str__(self):
        return self.user.username
# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    locality = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.name