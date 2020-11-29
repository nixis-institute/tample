from django.db import models

# Create your models here.

class Temple(models.Model):
    name = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    pincode = models.CharField(max_length=6)
    block = models.CharField(max_length=20)
    address = models.TextField()
    latitude = models.CharField(max_length=15)
    logitute = models.CharField(max_length=15)
    
    def __str__(self):
        return self.name+" "+self.pincode