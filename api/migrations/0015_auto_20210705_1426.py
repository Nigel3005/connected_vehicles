# Generated by Django 3.1.7 on 2021-07-05 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0014_auto_20210625_1319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehiclestatus',
            name='vehicle_id',
            field=models.CharField(max_length=20),
        ),
    ]
