# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Outward(models.Model):
    outward_id = models.AutoField(primary_key=True)
    outward_clientid = models.IntegerField()
    outward_date = models.DateField()
    outward_uploaddocstatus = models.IntegerField()
    outward_inwardid = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'outward'