# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class PendingWork(models.Model):
    PendingWork_employeeid = models.IntegerField()
    PendingWork_inwardid = models.IntegerField()
    PendingWork_name = models.CharField(max_length=256)
    PendingWork_postid = models.AutoField(primary_key=True)

    class Meta:
        managed = True
        db_table = 'pending_work'
