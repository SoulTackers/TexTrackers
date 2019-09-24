# Generated by Django 2.2.5 on 2019-09-24 15:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Client', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clientaccountantinfo',
            name='client_id',
        ),
        migrations.RemoveField(
            model_name='clientbankinfo',
            name='client_id',
        ),
        migrations.RemoveField(
            model_name='clientlegalinfo',
            name='client_id',
        ),
        migrations.RemoveField(
            model_name='clientpassword',
            name='client_id',
        ),
        migrations.RemoveField(
            model_name='clientsevice',
            name='client_id',
        ),
        migrations.AddField(
            model_name='clientaccountantinfo',
            name='client',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Client.Client'),
        ),
        migrations.AddField(
            model_name='clientbankinfo',
            name='client',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Client.Client'),
        ),
        migrations.AddField(
            model_name='clientlegalinfo',
            name='client',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Client.Client'),
        ),
        migrations.AddField(
            model_name='clientpassword',
            name='client',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Client.Client'),
        ),
        migrations.AddField(
            model_name='clientsevice',
            name='client',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Client.Client'),
        ),
    ]
