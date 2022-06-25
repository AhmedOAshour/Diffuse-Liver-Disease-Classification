
from distutils.command.upload import upload
from time import strftime
from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.contrib.postgres.fields import JSONField
from datetime import datetime
from django import forms

# Create your models here.

class Doctor(models.Model):
    name = models.CharField(max_length = 200)
    username = models.CharField(max_length = 200)
    password = models.CharField(max_length = 200, null=True)
    email = models.EmailField(max_length=200, null=True, default='')
    assigned_patients = models.TextField(null = True, blank = True)
    role = models.CharField(max_length=200, default="doctor")

    def __str__(self):
        return self.name

class Admin(models.Model):
    name = models.CharField(max_length = 200)
    username = models.CharField(max_length = 200)
    password = models.CharField(max_length = 200, null=True)
    role = models.CharField(max_length=200, default="admin")

    def __str__(self):
        return self.name

class Patient(models.Model):

    M = "Male"
    F = "Female"

    GENDER_CHOICES = (
        (M, "Male"),
        (F, "Female")
    )


    def get_email_default():
        return '1, 2, 3, 4'.split(', ')


    patient_name = models.CharField(max_length = 200)
    username = models.CharField(max_length = 200)
    password = models.CharField(max_length = 200, null=True)
    phone_num = models.CharField(max_length = 13)
    birth_date = models.DateField()
    gender = models.CharField(choices=GENDER_CHOICES, max_length=50, null=True, default='')
    email = models.EmailField(max_length=200, null=True, default='')
    # medical_conditions = ArrayField(models.CharField(max_length=200, blank=True))
    medical_conditions = models.CharField(max_length = 200, null=True, blank=True)
 
    assigned_doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    check_in_date = models.DateField(auto_now_add = True)
    role = models.CharField(max_length=200, default="patient")

    def __str__(self):
        return self.patient_name

class Report(models.Model):
    patient= models.CharField(max_length = 13)
    doctor = models.CharField(max_length = 13)
    notes = models.TextField(null = True, blank = True)
    image = models.ImageField(upload_to='scans/', height_field=None, width_field=None, max_length=None, blank=True)
    date = models.DateField(auto_now_add = True)
    classification = models.TextField(null = True, blank = True)
    diagnosis = models.TextField(null = True, blank = True)

    def __int__(self):
        return self.patient
         
class Scan(models.Model):
    scan = models.ImageField(upload_to='scans/')

    def __int__(self):
        return self.id
