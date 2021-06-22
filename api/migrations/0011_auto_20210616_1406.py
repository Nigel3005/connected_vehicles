# Generated by Django 3.1.7 on 2021-06-16 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_auto_20210527_1142'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vehiclestatus',
            name='accu_spanning',
        ),
        migrations.RemoveField(
            model_name='vehiclestatus',
            name='cell_percentage',
        ),
        migrations.RemoveField(
            model_name='vehiclestatus',
            name='cell_spanning',
        ),
        migrations.AddField(
            model_name='vehiclestatus',
            name='actieradius',
            field=models.CharField(default=0, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vehiclestatus',
            name='airco',
            field=models.CharField(default=0, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vehiclestatus',
            name='batterij_gemiddeld',
            field=models.CharField(default=0, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vehiclestatus',
            name='batterij_percentage',
            field=models.CharField(default=0, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vehiclestatus',
            name='batterij_temperatuur',
            field=models.CharField(default=0, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vehiclestatus',
            name='controller_temperatuur',
            field=models.CharField(default=0, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vehiclestatus',
            name='error',
            field=models.CharField(default=0, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vehiclestatus',
            name='snelheid',
            field=models.CharField(default=0, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vehiclestatus',
            name='trilling',
            field=models.CharField(default=0, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vehiclestatus',
            name='vermogen',
            field=models.CharField(default=0, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vehiclestatus',
            name='verwarming',
            field=models.CharField(default=0, max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='vehiclestatus',
            name='laden',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='vehiclestatus',
            name='motor_temperatuur',
            field=models.CharField(max_length=20),
        ),
    ]