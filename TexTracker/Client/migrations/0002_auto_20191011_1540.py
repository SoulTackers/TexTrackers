# Generated by Django 2.2.3 on 2019-10-11 10:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Client', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='client_service_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='Client.Services'),
        ),
        migrations.DeleteModel(
            name='ClientSevice',
        ),
    ]
