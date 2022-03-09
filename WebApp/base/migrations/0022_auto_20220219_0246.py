# Generated by Django 3.2.12 on 2022-02-19 00:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0021_alter_report_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='check_in_date',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='report',
            name='image',
            field=models.ImageField(upload_to='static/images/scans/'),
        ),
    ]