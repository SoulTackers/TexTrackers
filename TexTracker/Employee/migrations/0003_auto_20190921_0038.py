# Generated by Django 2.2.5 on 2019-09-20 23:38

from django.db import migrations
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('Employee', '0002_auto_20190920_2035'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='last_login',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='password',
        ),
        migrations.AlterField(
            model_name='employee',
            name='employee_phone',
            field=phone_field.models.PhoneField(max_length=31),
        ),
    ]
