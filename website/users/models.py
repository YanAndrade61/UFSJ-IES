from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from phone_field import PhoneField

# Create your models here.


class UserStudent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(blank=True, null=True, max_length=50)
    cpf = models.CharField(blank=True, null=True, max_length=11)
    gender = models.CharField(blank=True, null=True, max_length=250)
    email = models.CharField(blank=True, null=True, max_length=250)
    phone_number = PhoneField()
    birth_date = models.DateTimeField()

    def __str__(self):
        return self.user.username