# Generated by Django 2.2.5 on 2019-10-01 17:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeePost',
            fields=[
                ('ep_id', models.AutoField(primary_key=True, serialize=False)),
                ('ep_details', models.TextField(blank=True, null=True)),
                ('ep_name', models.CharField(blank=True, max_length=256, null=True)),
            ],
            options={
                'db_table': 'employee_post',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('employee_id', models.AutoField(primary_key=True, serialize=False)),
                ('employee_name', models.CharField(blank=True, max_length=256, null=True)),
                ('employee_phone', models.CharField(blank=True, max_length=10, null=True)),
                ('employee_postid', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Employee.EmployeePost')),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'employee',
                'managed': True,
            },
        ),
    ]
