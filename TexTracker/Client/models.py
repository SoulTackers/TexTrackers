# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from phone_field import PhoneField
# Create your models here.
class AccountType(models.Model):
    account_type_id = models.AutoField(primary_key=True)
    account_type_name = models.CharField(max_length=60)
    account_type_details = models.TextField()

    class Meta:
        managed = True
        db_table = 'account_type'


class Client(models.Model):
    client_id = models.AutoField(primary_key=True)
    client_name = models.TextField()
    client_account_type = models.IntegerField()
    client_office_address1 = models.TextField()
    client_office_address2 = models.TextField()
    client_office_pin = models.CharField(max_length=12)
    # https://stackoverflow.com/questions/19130942/whats-the-best-way-to-store-phone-number-in-django-models
    client_phone = PhoneField()
    client_email = models.EmailField()
    client_type_of_dealer = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'client'


class ClientAccountantInfo(models.Model):
    client_acc_info_accountant_name = models.TextField()
    client_acc_info_accountant_phone = models.BigIntegerField()
    client_acc_info_accountant_email = models.EmailField()
    client_acc_info_accountant_counsultant_name = models.TextField()
    client_acc_info_accountant_counsultant_phone = PhoneField()
    client_acc_info_accountant_counsultant_email = models.EmailField()
    client_acc_info_ca_name = models.TextField()
    client_acc_info_ca_phone = PhoneField()
    client_acc_info_ca_email = models.EmailField()
    client_id = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'client_accountant_info'


class ClientBankInfo(models.Model):
    client_id = models.IntegerField()
    client_bank_info_bank_name = models.TextField()
    client_bank_info_account_no = models.BigIntegerField()
    client_bank_info_branch = models.TextField()

    class Meta:
        managed = True
        db_table = 'client_bank_info'


class ClientLegalInfo(models.Model):
    client_leg_info_date_of_incorporation = models.DateField()
    client_leg_info_st_file_no = models.BigIntegerField(db_column='client_leg_info_ST_file_no')  # Field name made lowercase.
    client_leg_info_it_file_no = models.BigIntegerField(db_column='client_leg_info_IT_file_no')  # Field name made lowercase.
    client_leg_info_tds_file_no = models.BigIntegerField(db_column='client_leg_info_TDS_file_no')  # Field name made lowercase.
    client_leg_info_vat_file_no = models.BigIntegerField(db_column='client_leg_info_VAT_file_no')  # Field name made lowercase.
    client_leg_info_vat_audit_file_no = models.BigIntegerField(db_column='client_leg_info_VAT_audit_file_no')  # Field name made lowercase.
    client_leg_info_exercise_file_no = models.BigIntegerField()
    client_leg_info_vat_tin_no = models.BigIntegerField(db_column='client_leg_info_VAT_tin_no')  # Field name made lowercase.
    client_leg_info_date1 = models.DateField()
    client_leg_info_cst_tin_no = models.BigIntegerField(db_column='client_leg_info_CST_tin_no')  # Field name made lowercase.
    client_leg_info_date2 = models.DateField()
    client_leg_info_service_tax_no = models.BigIntegerField()
    client_leg_info_date3 = models.DateField()
    client_leg_info_ecc_no = models.BigIntegerField(db_column='client_leg_info_ECC_no')  # Field name made lowercase.
    client_leg_info_date4 = models.DateField()
    client_leg_info_pancard_no = models.BigIntegerField()
    client_leg_info_tds_no = models.BigIntegerField(db_column='client_leg_info_TDS_no')  # Field name made lowercase.
    client_leg_info_firm_registration = models.BigIntegerField()
    client_leg_info_iec_no = models.BigIntegerField(db_column='client_leg_info_IEC_no')  # Field name made lowercase.
    client_leg_info_elect_no = models.BigIntegerField()
    client_leg_info_pte1 = models.BigIntegerField(db_column='client_leg_info_PTE1')  # Field name made lowercase.
    client_leg_info_pte2 = models.BigIntegerField(db_column='client_leg_info_PTE2')  # Field name made lowercase.


    ###############################################
    client_id = models.IntegerField()
    ###############################################

    class Meta:
        managed = True
        db_table = 'client_legal_info'


class ClientPassword(models.Model):
    client_id = models.IntegerField()
    client_password_vat = models.TextField(db_column='client_password_VAT')  # Field name made lowercase.
    client_password_it = models.TextField(db_column='client_password_IT')  # Field name made lowercase.
    client_passwordclient_password_tds = models.TextField(db_column='client_passwordclient_password_TDS')  # Field name made lowercase.
    client_password_st = models.TextField(db_column='client_password_ST')  # Field name made lowercase.
    client_password_excise = models.TextField()
    client_password_vat_unique_id = models.TextField(db_column='client_password_VAT_unique_id')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'client_password'


class ClientSevice(models.Model):
    client_id = models.IntegerField()
    client_service_id = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'client_sevice'
