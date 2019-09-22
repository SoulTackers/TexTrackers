# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import datetime

# Create your models here.


class Inward(models.Model):
    inward_id = models.AutoField(primary_key=True)
    inward_mode_id = models.IntegerField()
    inward_track = models.TextField()
    inward_employeeid = models.IntegerField()
    inward_posttype = models.CharField(max_length=255)
    inward_returnperiod = models.DateTimeField(default=datetime.date.today)
    inward_month = models.DecimalField(max_digits=2, decimal_places=0)
    inward_year = models.IntegerField()  # This field type is a guess.
    # inward_uploadfilestatus = models.IntegerField()
    inward_remarks = models.TextField()
    inward_client_id = models.IntegerField()
    inward_date = models.DateField(default=datetime.date.today)

    class Meta:
        managed = True
        db_table = 'inward'


class InwardPostType(models.Model):
    InwardPostType_id = models.AutoField(primary_key=True)
    InwardPostType_name = models.CharField(max_length=255)
    InwardPostType_details = models.CharField(max_length=255)

    class Meta:
        managed = True
        db_table = 'inward_post_type'


class InwardTypes(models.Model):
    InwardTypes_id = models.AutoField(primary_key=True)
    InwardTypes_name = models.CharField(max_length=255)
    InwardTypes_details = models.CharField(max_length=255)

    class Meta:
        managed = True
        db_table = 'inward_types'

class InwardDocument(models.Model):
    inward_id = models.OneToOneField(Inward, models.CASCADE)
    inward_doc = models.FileField(upload_to='uploads/')
    class Meta:
        managed = True
        db_table = 'inward_Document'
