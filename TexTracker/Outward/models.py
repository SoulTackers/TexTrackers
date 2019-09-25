# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from FeesInward.models import Inward
from Client.models import Client
from django.db import models
from django.urls import reverse

# Create your models here.


class Outward(models.Model):
    outward_id = models.AutoField(primary_key=True)
    outward_cid = models.ForeignKey(Client,on_delete=models.CASCADE, null=True, blank=True)
    outward_date = models.DateField(blank=True,null=True)
    outward_uploaddocstatus = models.IntegerField(blank=True,null=True)
    outward_iid = models.ForeignKey(Inward,on_delete=models.CASCADE,blank=True,null=True) 
    

    class Meta:
        managed = True
        db_table = 'outward'

