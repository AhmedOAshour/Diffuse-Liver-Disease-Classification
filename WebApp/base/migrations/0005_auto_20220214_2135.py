# Generated by Django 3.2.12 on 2022-02-14 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_auto_20220214_2130'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='notes',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='assigned_patients',
            field=models.TextField(blank=True, null=True),
        ),
    ]
