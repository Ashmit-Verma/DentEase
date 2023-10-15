from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    locality = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.name