from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    is_user = models.BooleanField(default=False)
    is_hospital = models.BooleanField(default=False)


class hspinfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    hospital_Name = models.CharField(max_length=50)
    phone = models.CharField(max_length=12)
    email = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    address = models.CharField(max_length=120)
    no_of_beds = models.CharField(max_length=10)
    no_of_ventilators = models.CharField(max_length=10)
    no_of_vaccines = models.CharField(max_length=10)

    def __str__(self):
        return self.user.username

class usrinfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_Name = models.CharField(max_length=50)
    phone = models.CharField(max_length=12)
    email = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    address = models.TextField()
    

    def __str__(self):
        return self.user.username