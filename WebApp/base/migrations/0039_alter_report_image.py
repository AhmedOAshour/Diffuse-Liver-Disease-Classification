# Generated by Django 3.2.12 on 2022-03-09 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0038_delete_model'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='image',
            field=models.ImageField(blank=True, upload_to='scans/'),
        ),
    ]
