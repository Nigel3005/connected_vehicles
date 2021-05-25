# Generated by Django 3.1.7 on 2021-05-25 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_vehiclestatus_time'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vehiclestatus',
            old_name='test_1',
            new_name='accu_spanning',
        ),
        migrations.RenameField(
            model_name='vehiclestatus',
            old_name='test_2',
            new_name='cell_perc',
        ),
        migrations.AddField(
            model_name='vehiclestatus',
            name='cell_spanning',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vehiclestatus',
            name='laden',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vehiclestatus',
            name='motor_temp',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]