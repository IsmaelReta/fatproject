# Generated by Django 4.1 on 2022-08-25 11:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_certificate_status_healthinsurance_description_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='healthinsurance',
            old_name='person_id',
            new_name='person',
        ),
        migrations.RenameField(
            model_name='person',
            old_name='user_id',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='tutor',
            old_name='person_id',
            new_name='person',
        ),
    ]