# Generated by Django 4.1 on 2022-09-13 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0002_tutor_healthinsurance_certificate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certificate',
            name='image',
            field=models.ImageField(upload_to='patient/images'),
        ),
    ]