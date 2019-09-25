# Generated by Django 2.2.3 on 2019-09-24 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FeesInward', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feesinward',
            name='feesinward_amount',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='feesinward',
            name='feesinward_balance_outstanding',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='feesinward',
            name='feesinward_client_id',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='feesinward',
            name='feesinward_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='feesinward',
            name='feesinward_discount',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='feesinward',
            name='feesinward_employee_id',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='feesinward',
            name='feesinward_inward_mode_id',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='feesinward',
            name='feesinward_paymentdetails',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='feesinward',
            name='feesinward_paymenttype',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]