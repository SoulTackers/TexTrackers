# Generated by Django 2.2.5 on 2019-09-28 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inward', '0002_pendingdocument'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inward',
            name='inward_uploadfilestatus',
            field=models.BooleanField(),
        ),
    ]
