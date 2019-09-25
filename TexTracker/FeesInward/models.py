# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from Inward.models import Inward,InwardPostType,InwardTypes
from django.db import models

# Create your models here.

class Feesinward(models.Model):
    feesinward_id = models.AutoField(primary_key=True)
    feesinward_date = models.DateField(blank=True,null=True)
    feesinward_inward_mode_id = models.IntegerField(blank=True,null=True)
    feesinward_employee_id = models.IntegerField(blank=True,null=True)
    feesinward_discount = models.FloatField(blank=True,null=True)
    feesinward_balance_outstanding = models.FloatField(blank=True,null=True)
    feesinward_paymentdetails = models.TextField(blank=True,null=True)
    feesinward_paymenttype = models.CharField(max_length=255,blank=True,null=True)
    feesinward_amount = models.FloatField(blank=True,null=True)
    feesinward_client_id = models.IntegerField(blank=True,null=True)

    class Meta:
        managed = True
        db_table = 'feesinward'

class PaymentType(models.Model):
    paymenttype_id = models.AutoField(primary_key=True)
    paymenttype_details = models.TextField(blank=True,null=True)
    paymenttype_name = models.CharField(max_length=255,blank=True,null=True)

    class Meta:
        managed=True
        db_table = 'paymenttype'