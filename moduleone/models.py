from django.db import models
from django.core.exceptions import ValidationError
# Create your models here.

class ActiveItems(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(active='Y')



def checkclcemail(val):
    if '@clc.in' not in val:
        raise ValidationError('Not a valid Email address')

def checkminsal(val):
    if val<25000.0:
        raise ValidationError('Less salary.!')

class Hospital(models.Model):
    name=models.CharField('hs_name',max_length=100)
    active=models.CharField('active',default='Y',max_length=10)
    address=models.OneToOneField('Address',on_delete=models.CASCADE,related_name='hospital',null=True)
    activent = ActiveItems()
    allen = models.Manager()


class Doctor(models.Model):
    name=models.CharField('dt_name',max_length=100)
    spec=models.CharField('dt_spc',max_length=100)
    yrofexp = models.IntegerField()
    salary = models.FloatField(validators=[checkminsal])
    email = models.EmailField(max_length=100,validators=[checkclcemail])
    blog = models.SlugField(max_length=300)
    active = models.CharField('active',max_length=10, default='Y')
    hospital = models.ForeignKey(Hospital,on_delete=models.CASCADE,related_name='doctors',null=True)
    activent = ActiveItems()
    allen = models.Manager()

class Patient(models.Model):
    name=models.CharField('pt_name',max_length=100)
    balance = models.FloatField()
    bldgrp = models.CharField(max_length=100)
    diseases = models.CharField(max_length=100)
    active = models.CharField('active', max_length=10,default='Y')
    doctors = models.ManyToManyField(Doctor,related_name='patients')
    address = models.ForeignKey('Address', on_delete=models.CASCADE,related_name='patients',null=True)
    allen = models.Manager()
    activent = ActiveItems()

class Address(models.Model):
    city=models.CharField('city',max_length=100)
    state = models.CharField('state', max_length=100)
    pincode = models.IntegerField('pincode')
    active = models.CharField('active', max_length=10,default='Y')
    allen = models.Manager()
    activent = ActiveItems()

'''
H-D -- 1m
H-A -- 11
D-P--MM
P-A -- M-1
'''

