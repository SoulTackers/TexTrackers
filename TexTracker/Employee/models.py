# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from phone_field import PhoneField

class EmployeePost(models.Model):
    ep_id = models.AutoField(primary_key=True)
    ep_details = models.TextField(blank=True,null=True)
    ep_name = models.CharField(max_length=256,blank=True,null=True)

    class Meta:
        managed = True
        db_table = 'employee_post'

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,blank=True,null=True)
    employee_id = models.AutoField(primary_key=True)
    employee_name = models.CharField(max_length=256,blank=True,null=True)
    employee_postid = models.ForeignKey(EmployeePost, on_delete=models.CASCADE,blank=True,null=True)
    employee_phone = models.CharField(max_length=10,blank=True,null=True)
    class Meta:
        managed = True
        db_table = 'employee'
