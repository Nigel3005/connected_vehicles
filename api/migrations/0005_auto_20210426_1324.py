# Generated by Django 3.1.7 on 2021-04-26 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20210423_1243'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehiclestatus',
            name='test_1',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vehiclestatus',
            name='test_2',
            field=models.CharField(default=2, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vehiclestatus',
            name='vehicle_name',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
    ]
