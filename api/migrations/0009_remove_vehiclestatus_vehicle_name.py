# Generated by Django 3.1.7 on 2021-05-26 14:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_remove_vehiclestatus_payload'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vehiclestatus',
            name='vehicle_name',
        ),
    ]
