# Generated by Django 3.2.12 on 2022-02-19 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0031_auto_20220220_0031'),
    ]

    operations = [
        migrations.AddField(
            model_name='admin',
            name='password',
            field=models.CharField(max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='doctor',
            name='password',
            field=models.CharField(max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='patient',
            name='password',
            field=models.CharField(max_length=200),
            preserve_default=False,
        ),
    ]
