# Generated by Django 3.1.7 on 2021-05-27 09:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_remove_vehiclestatus_vehicle_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vehiclestatus',
            old_name='cell_perc',
            new_name='cell_percentage',
        ),
        migrations.RenameField(
            model_name='vehiclestatus',
            old_name='motor_temp',
            new_name='motor_temparatuur',
        ),
    ]