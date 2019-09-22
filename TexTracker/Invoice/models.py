# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Invoice(models.Model):
    invoice_id = models.AutoField(primary_key=True)
    invoice_servicetype = models.CharField(max_length=255)
    invoice_address = models.TextField()
    invoice_amount = models.FloatField()
    # invoice_uploadfilestatus = models.IntegerField()
    invoice_comments = models.TextField()
    invoice_clientid = models.IntegerField()
    invoice_date = models.DateField()

    class Meta:
        managed = True
        db_table = 'invoice'

