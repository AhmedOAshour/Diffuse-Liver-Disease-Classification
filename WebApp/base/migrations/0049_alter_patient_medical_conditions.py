# Generated by Django 3.2.12 on 2022-06-22 21:51

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0048_patient_medical_conditions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='medical_conditions',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=200, null=True), size=None),
        ),
    ]
