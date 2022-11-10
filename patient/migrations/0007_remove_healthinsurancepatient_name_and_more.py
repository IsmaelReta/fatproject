# Generated by Django 4.1 on 2022-09-16 14:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('healthinsurance', '0001_initial'),
        ('patient', '0006_patient_birth_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='healthinsurancepatient',
            name='name',
        ),
        migrations.AddField(
            model_name='healthinsurancepatient',
            name='healthinsurance',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, related_name='patient', to='healthinsurance.healthinsurance'),
            preserve_default=False,
        ),
    ]