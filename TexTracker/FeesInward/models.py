# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from Inward.models import Inward,InwardPostType,InwardTypes
from django.db import models
from Employee.models import Employee
from Client.models import Client

# Create your models here.

class PaymentType(models.Model):
    paymenttype_id = models.AutoField(primary_key=True)
    paymenttype_details = models.TextField(blank=True,null=True)
    paymenttype_name = models.CharField(max_length=255,blank=True,null=True)

    def __str__(self):
        return self.paymenttype_name

    class Meta:
        managed=True
        db_table = 'paymenttype'



class Feesinward(models.Model):
    feesinward_id = models.AutoField(primary_key=True)
    feesinward_date = models.DateField(blank=True,null=True)
    feesinward_inward_mode_id = models.ForeignKey(InwardTypes,on_delete=models.CASCADE,blank=True,null=True)     #here inward mode id = inwardtype id
    feesinward_employee_id = models.ForeignKey(Employee,on_delete=models.CASCADE,blank=True,null=True)
    feesinward_discount = models.FloatField(blank=True,null=True)
    feesinward_balance_outstanding = models.FloatField(blank=True,null=True)
    feesinward_paymenttype = models.ForeignKey(PaymentType,on_delete=models.CASCADE,blank=True,null=True)
    feesinward_amount = models.FloatField(blank=True,null=True)
    feesinward_client_id = models.ForeignKey(Client,on_delete=models.CASCADE,blank=True,null=True)

    class Meta:
        managed = True
        db_table = 'feesinward'

