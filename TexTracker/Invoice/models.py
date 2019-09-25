# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Invoice(models.Model):
    invoice_id = models.AutoField(primary_key=True)
    invoice_servicetype = models.CharField(max_length=255,blank=True,null=True)
    invoice_address = models.TextField(blank=True,null=True)
    invoice_amount = models.FloatField(blank=True,null=True)
    # invoice_uploadfilestatus = models.IntegerField()
    invoice_comments = models.TextField(blank=True,null=True)
    invoice_clientid = models.IntegerField(blank=True,null=True)
    invoice_date = models.DateField(blank=True,null=True)

    class Meta:
        managed = True
        db_table = 'invoice'

