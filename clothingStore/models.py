from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.utils import timezone

# Create your models here.


class Clothing(models.Model):
    author = models.CharField(max_length=30)
    title = models.CharField(max_length=30)
    description = models.TextField()
    pub_date = models.DateField(default=timezone.now())

    def __str__(self):
        return self.author


class Contact(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    phone_number = PhoneNumberField()
    fax_number = PhoneNumberField(blank=True)

    def __str__(self):
        return self.name


class RegistrationData(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=128)

    def __str__(self):
        return self.username

