# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Feesinward(models.Model):
    feesinward_id = models.AutoField(primary_key=True)
    feesinward_date = models.DateField()
    feesinward_inward_mode_id = models.IntegerField()
    feesinward_employee_id = models.IntegerField()
    feesinward_discount = models.FloatField()
    feesinward_balance_outstanding = models.FloatField()
    feesinward_paymentdetails = models.TextField()
    feesinward_paymenttype = models.CharField(max_length=255)
    feesinward_amount = models.FloatField()
    feesinward_client_id = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'feesinward'

