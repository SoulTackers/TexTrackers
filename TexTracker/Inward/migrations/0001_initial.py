# Generated by Django 2.2.3 on 2019-09-18 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Inward',
            fields=[
                ('inward_id', models.AutoField(primary_key=True, serialize=False)),
                ('inward_mode_id', models.IntegerField()),
                ('inward_track', models.TextField()),
                ('inward_employeeid', models.IntegerField()),
                ('inward_posttype', models.CharField(max_length=255)),
                ('inward_returnperiod', models.DateTimeField()),
                ('inward_month', models.DecimalField(decimal_places=0, max_digits=2)),
                ('inward_year', models.IntegerField()),
                ('inward_remarks', models.TextField()),
                ('inward_client_id', models.IntegerField()),
                ('inward_date', models.DateField()),
            ],
            options={
                'db_table': 'inward',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='InwardPostType',
            fields=[
                ('InwardPostType_id', models.AutoField(primary_key=True, serialize=False)),
                ('InwardPostType_name', models.CharField(max_length=255)),
                ('InwardPostType_details', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'inward_post_type',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='InwardTypes',
            fields=[
                ('InwardTypes_id', models.AutoField(primary_key=True, serialize=False)),
                ('InwardTypes_name', models.CharField(max_length=255)),
                ('InwardTypes_details', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'inward_types',
                'managed': True,
            },
        ),
    ]
