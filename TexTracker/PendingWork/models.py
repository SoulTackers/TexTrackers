# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from Inward.models import Inward
from Employee.models import Employee,EmployeePost
from django.db import models

# Create your models here.

class PendingWork(models.Model):
    PendingWork_employeeid = models.IntegerField(blank=True,null=True) #Employee,on_delete=models.CASCADE, --> foreign key
    PendingWork_inwardid = models.IntegerField(blank=True,null=True)   #Inward,on_delete=models.CASCADE, --> foreign key
    PendingWork_name = models.CharField(max_length=256,blank=True,null=True)
    PendingWork_postid = models.AutoField(primary_key=True)

    class Meta:
        managed = True
        db_table = 'pending_work'

