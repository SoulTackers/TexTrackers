# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Employee(models.Model):
    employee_id = models.AutoField(primary_key=True)
    employee_name = models.CharField(max_length=256)
    employee_postid = models.IntegerField()
    employee_phone = models.IntegerField()
# pip install django-phonenumber-field
#PhoneNumberField
    class Meta:
        managed = True
        db_table = 'employee'


class EmployeePost(models.Model):
    ep_id = models.AutoField(primary_key=True)
    ep_details = models.TextField()
    ep_name = models.CharField(max_length=256)

    class Meta:
        managed = True
        db_table = 'employee_post'

