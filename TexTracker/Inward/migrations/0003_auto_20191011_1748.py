# Generated by Django 2.2.5 on 2019-10-11 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inward', '0002_auto_20191009_0135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inwarddocument',
            name='inward_doc',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/'),
        ),
    ]
