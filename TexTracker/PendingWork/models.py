# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from Inward.models import Inward
from Employee.models import Employee,EmployeePost
from django.db import models

# Create your models here.

class PendingWork(models.Model):
    Pendingwork_id = models.AutoField(primary_key=True)
    PendingWork_employeeid = models.ForeignKey(Employee,on_delete=models.CASCADE, blank=True, null=True)
    PendingWork_inwardid = models.OneToOneField(Inward, on_delete=models.CASCADE, blank=True,null=True)

    class Meta:
        managed = True
        db_table = 'pending_work'
