# Generated by Django 2.2.5 on 2019-09-26 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('invoice_id', models.AutoField(primary_key=True, serialize=False)),
                ('invoice_servicetype', models.CharField(blank=True, max_length=255, null=True)),
                ('invoice_address', models.TextField(blank=True, null=True)),
                ('invoice_amount', models.FloatField(blank=True, null=True)),
                ('invoice_comments', models.TextField(blank=True, null=True)),
                ('invoice_clientid', models.IntegerField(blank=True, null=True)),
                ('invoice_date', models.DateField(blank=True, null=True)),
            ],
            options={
                'db_table': 'invoice',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Servicetype',
            fields=[
                ('servicetype_id', models.AutoField(primary_key=True, serialize=False)),
                ('servicetype_name', models.CharField(max_length=255)),
                ('servicetype_details', models.TextField()),
            ],
            options={
                'db_table': 'servicetype',
                'managed': True,
            },
        ),
    ]
