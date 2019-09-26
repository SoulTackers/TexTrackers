# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from Inward.models import Inward
from Employee.models import Employee,EmployeePost
from Client.models import Client
from django.db import models

# Create your models here.

class PendingWork(models.Model):
    PendingWork_employeeid = models.ForeignKey(Employee,on_delete=models.CASCADE, null=True, blank=True)
    PendingWork_inwardid = models.OneToOneField(Inward, on_delete=models.CASCADE, null=True, blank=True)
    PendingWork_clientid = models.ForeignKey(Client,on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        managed = True
        db_table = 'pending_work'

