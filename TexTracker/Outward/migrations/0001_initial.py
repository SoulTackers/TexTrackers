# Generated by Django 2.2.5 on 2019-09-26 15:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Client', '0001_initial'),
        ('Inward', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Outward',
            fields=[
                ('outward_id', models.AutoField(primary_key=True, serialize=False)),
                ('outward_date', models.DateField(blank=True, null=True)),
                ('outward_uploaddocstatus', models.IntegerField(blank=True, null=True)),
                ('outward_cid', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Client.Client')),
                ('outward_iid', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Inward.Inward')),
            ],
            options={
                'db_table': 'outward',
                'managed': True,
            },
        ),
    ]
