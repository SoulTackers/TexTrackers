# Generated by Django 2.2.3 on 2019-10-11 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Client', '0002_auto_20191011_1540'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='client_name',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
    ]