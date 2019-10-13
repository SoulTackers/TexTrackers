# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from Client.models import Client
from Employee.models import Employee
from django.db import models
import datetime

# Create your models here.

class InwardTypes(models.Model):       # Here inward mode = inward type
    InwardTypes_id = models.AutoField(primary_key=True)
    InwardTypes_name = models.CharField(max_length=255,blank=True,null=True)
    InwardTypes_details = models.CharField(max_length=255,blank=True,null=True)

    def __str__(self):
        return self.InwardTypes_name

    class Meta:
        managed = True
        db_table = 'inward_types'


class InwardPostType(models.Model):
    InwardPostType_id = models.AutoField(primary_key=True)
    InwardPostType_name = models.CharField(max_length=255,blank=True,null=True)
    InwardPostType_details = models.CharField(max_length=255,blank=True,null=True)

    def __str__(self):
        return self.InwardPostType_name

    class Meta:
        managed = True
        db_table = 'inward_post_type'


class Inward(models.Model):
    inward_id = models.AutoField(primary_key=True)
    # inward_mode_id = models.IntegerField(blank=True,null=True)
    inward_track = models.TextField(blank=True,null=True)
    inward_employeeid = models.ForeignKey(Employee,on_delete=models.CASCADE,blank=True,null=True)
    inward_type = models.ForeignKey(InwardTypes,on_delete=models.CASCADE,blank=True,null=True)
    inward_posttype = models.ForeignKey(InwardPostType,on_delete=models.CASCADE,blank=True,null=True)
    inward_returnperiod = models.DateTimeField(default=datetime.date.today,blank=True,null=True)
    inward_month = models.DecimalField(max_digits=2, decimal_places=0,blank=True,null=True)
    inward_year = models.IntegerField(blank=True,null=True)  # This field type is a guess.
    inward_uploadfilestatus = models.BooleanField(blank=True,null=True)
    inward_remarks = models.TextField(blank=True,null=True)
    inward_client_id = models.ForeignKey(Client,on_delete=models.CASCADE,blank=True,null=True)
    inward_date = models.DateField(default=datetime.date.today,blank=True,null=True)

    class Meta:
        managed = True
        db_table = 'inward'

class InwardPendingDocument(models.Model):
    inward = models.OneToOneField(Inward, models.CASCADE,blank=True,null=True)
    class meta:
        managed = True
        db_table = 'pending_inward_document'


class InwardDocument(models.Model):
    inward_id = models.OneToOneField(Inward, models.CASCADE,blank=True,null=True)
    inward_doc = models.FileField(upload_to='uploads/',default='default.png')
    class Meta:
        managed = True
        db_table = 'inward_Document'
