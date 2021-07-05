# Generated by Django 3.1.7 on 2021-06-25 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_auto_20210623_1629'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehiclestatus',
            name='aantal_satellieten',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='vehiclestatus',
            name='actieradius',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='vehiclestatus',
            name='airco_aan',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='vehiclestatus',
            name='airco_actief',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='vehiclestatus',
            name='batterij_percentage',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='vehiclestatus',
            name='batterij_temperatuur',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='vehiclestatus',
            name='batterijspanning_gemiddeld',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='vehiclestatus',
            name='batterijspanning_maximum',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='vehiclestatus',
            name='batterijspanning_minimum',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='vehiclestatus',
            name='bedrijfstijd',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='vehiclestatus',
            name='controller_temperatuur',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='vehiclestatus',
            name='controller_temperatuur_alarm',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='vehiclestatus',
            name='error_12v',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='vehiclestatus',
            name='gemiddeld_verbruik',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='vehiclestatus',
            name='hoogspanningserror',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='vehiclestatus',
            name='kabine_ingestelde_temperatuur',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='vehiclestatus',
            name='kabine_temperatuur',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='vehiclestatus',
            name='motor_temperatuur',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='vehiclestatus',
            name='motor_temperatuur_alarm',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='vehiclestatus',
            name='olie_temperatuur',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='vehiclestatus',
            name='snelheid',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='vehiclestatus',
            name='spanning_12v',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='vehiclestatus',
            name='vermogen',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='vehiclestatus',
            name='versnelling_x_richting',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='vehiclestatus',
            name='versnelling_y_richting',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='vehiclestatus',
            name='versnelling_z_richting',
            field=models.FloatField(),
        ),
    ]