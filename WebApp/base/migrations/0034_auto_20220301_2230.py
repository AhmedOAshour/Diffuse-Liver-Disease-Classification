# Generated by Django 3.2.12 on 2022-03-01 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0033_alter_admin_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='password',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='password',
            field=models.CharField(max_length=200, null=True),
        ),
    ]