# Generated by Django 3.2.12 on 2022-06-26 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0062_patient_is_archived'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='is_archived',
            field=models.BooleanField(default=False),
        ),
    ]
