# Generated by Django 4.1 on 2022-09-21 14:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('warehouse', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventory',
            name='warehouse',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='inventory', to='warehouse.warehouse'),
        ),
    ]