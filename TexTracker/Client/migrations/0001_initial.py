# Generated by Django 2.2.5 on 2019-09-26 15:39

from django.db import migrations, models
import django.db.models.deletion
import phone_field.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AccountType',
            fields=[
                ('account_type_id', models.AutoField(primary_key=True, serialize=False)),
                ('account_type_name', models.CharField(max_length=60)),
                ('account_type_details', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'account_type',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('client_id', models.AutoField(primary_key=True, serialize=False)),
                ('client_name', models.TextField()),
                ('client_office_address1', models.TextField(blank=True, null=True)),
                ('client_office_address2', models.TextField(blank=True, null=True)),
                ('client_office_pin', models.CharField(blank=True, max_length=12, null=True)),
                ('client_phone', phone_field.models.PhoneField(blank=True, max_length=31, null=True)),
                ('client_email', models.EmailField(blank=True, max_length=254, null=True)),
                ('client_type_of_dealer', models.IntegerField(blank=True, null=True)),
                ('client_account_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='Client.AccountType')),
            ],
            options={
                'db_table': 'client',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Services',
            fields=[
                ('service_id', models.AutoField(primary_key=True, serialize=False)),
                ('service_name', models.CharField(max_length=60)),
                ('service_details', models.TextField()),
            ],
            options={
                'db_table': 'Services',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='ClientSevice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Client.Client')),
                ('client_service_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='Client.Services')),
            ],
            options={
                'db_table': 'client_sevice',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='ClientPassword',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_password_vat', models.TextField(blank=True, db_column='client_password_VAT', null=True)),
                ('client_password_it', models.TextField(blank=True, db_column='client_password_IT', null=True)),
                ('client_passwordclient_password_tds', models.TextField(blank=True, db_column='client_passwordclient_password_TDS', null=True)),
                ('client_password_st', models.TextField(blank=True, db_column='client_password_ST', null=True)),
                ('client_password_excise', models.TextField(blank=True, null=True)),
                ('client_password_vat_unique_id', models.TextField(blank=True, db_column='client_password_VAT_unique_id', null=True)),
                ('client', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Client.Client')),
            ],
            options={
                'db_table': 'client_password',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='ClientLegalInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_leg_info_date_of_incorporation', models.DateField(blank=True, null=True)),
                ('client_leg_info_st_file_no', models.BigIntegerField(blank=True, db_column='client_leg_info_ST_file_no', null=True)),
                ('client_leg_info_it_file_no', models.BigIntegerField(blank=True, db_column='client_leg_info_IT_file_no', null=True)),
                ('client_leg_info_tds_file_no', models.BigIntegerField(blank=True, db_column='client_leg_info_TDS_file_no', null=True)),
                ('client_leg_info_vat_file_no', models.BigIntegerField(blank=True, db_column='client_leg_info_VAT_file_no', null=True)),
                ('client_leg_info_vat_audit_file_no', models.BigIntegerField(blank=True, db_column='client_leg_info_VAT_audit_file_no', null=True)),
                ('client_leg_info_exercise_file_no', models.BigIntegerField(blank=True, null=True)),
                ('client_leg_info_vat_tin_no', models.BigIntegerField(blank=True, db_column='client_leg_info_VAT_tin_no', null=True)),
                ('client_leg_info_date1', models.DateField(blank=True, null=True)),
                ('client_leg_info_cst_tin_no', models.BigIntegerField(blank=True, db_column='client_leg_info_CST_tin_no', null=True)),
                ('client_leg_info_date2', models.DateField(blank=True, null=True)),
                ('client_leg_info_service_tax_no', models.BigIntegerField(blank=True, null=True)),
                ('client_leg_info_date3', models.DateField(blank=True, null=True)),
                ('client_leg_info_ecc_no', models.BigIntegerField(blank=True, db_column='client_leg_info_ECC_no', null=True)),
                ('client_leg_info_date4', models.DateField(blank=True, null=True)),
                ('client_leg_info_pancard_no', models.BigIntegerField(blank=True, null=True)),
                ('client_leg_info_tds_no', models.BigIntegerField(blank=True, db_column='client_leg_info_TDS_no', null=True)),
                ('client_leg_info_firm_registration', models.BigIntegerField(blank=True, null=True)),
                ('client_leg_info_iec_no', models.BigIntegerField(blank=True, db_column='client_leg_info_IEC_no', null=True)),
                ('client_leg_info_elect_no', models.BigIntegerField(blank=True, null=True)),
                ('client_leg_info_pte1', models.BigIntegerField(blank=True, db_column='client_leg_info_PTE1', null=True)),
                ('client_leg_info_pte2', models.BigIntegerField(blank=True, db_column='client_leg_info_PTE2', null=True)),
                ('client', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Client.Client')),
            ],
            options={
                'db_table': 'client_legal_info',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='ClientBankInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_bank_info_bank_name', models.TextField(blank=True, null=True)),
                ('client_bank_info_account_no', models.BigIntegerField(blank=True, null=True)),
                ('client_bank_info_branch', models.TextField(blank=True, null=True)),
                ('client', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Client.Client')),
            ],
            options={
                'db_table': 'client_bank_info',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='ClientAccountantInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_acc_info_accountant_name', models.TextField(blank=True, null=True)),
                ('client_acc_info_accountant_phone', models.BigIntegerField(blank=True, null=True)),
                ('client_acc_info_accountant_email', models.EmailField(blank=True, max_length=254, null=True)),
                ('client_acc_info_accountant_counsultant_name', models.TextField(blank=True, null=True)),
                ('client_acc_info_accountant_counsultant_phone', phone_field.models.PhoneField(blank=True, max_length=31, null=True)),
                ('client_acc_info_accountant_counsultant_email', models.EmailField(blank=True, max_length=254, null=True)),
                ('client_acc_info_ca_name', models.TextField(blank=True, null=True)),
                ('client_acc_info_ca_phone', phone_field.models.PhoneField(blank=True, max_length=31, null=True)),
                ('client_acc_info_ca_email', models.EmailField(blank=True, max_length=254, null=True)),
                ('client', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Client.Client')),
            ],
            options={
                'db_table': 'client_accountant_info',
                'managed': True,
            },
        ),
    ]
