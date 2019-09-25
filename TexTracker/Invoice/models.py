# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from Client.models import Client
from django.db import models

# Create your models here.


class Invoice(models.Model):
    invoice_id = models.AutoField(primary_key=True)
    invoice_servicetype = models.CharField(max_length=255,blank=True,null=True)
    invoice_address = models.TextField(blank=True,null=True)
    invoice_amount = models.FloatField(blank=True,null=True)
    # invoice_uploadfilestatus = models.IntegerField()
    invoice_comments = models.TextField(blank=True,null=True)
    invoice_clientid = models.ForeignKey(Client,on_delete=models.CASCADE,blank=True,null=True)
    invoice_date = models.DateField(blank=True,null=True)

    class Meta:
        managed = True
        db_table = 'invoice'

class Servicetype(models.Model):
    servicetype_id = models.AutoField(primary_key=True)
    servicetype_name = models.CharField(max_length=255)
    servicetype_details = models.TextField()

    class Meta:
        managed = True
        db_table = 'servicetype'