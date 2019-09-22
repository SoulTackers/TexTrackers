# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from phone_field import PhoneField

class EmployeePost(models.Model):
    ep_id = models.AutoField(primary_key=True)
    ep_details = models.TextField()
    ep_name = models.CharField(max_length=256)

    def __str__(self):
        return self.ep_name

    class Meta:
        managed = True
        db_table = 'employee_post'

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    employee_id = models.AutoField(primary_key=True)
    employee_name = models.CharField(max_length=256)
    employee_postid = models.ForeignKey(EmployeePost, on_delete=models.DO_NOTHING)
    employee_phone = PhoneField()
# pip install django-phonenumber-field
#PhoneNumberField
    class Meta:
        managed = True
        db_table = 'employee'
