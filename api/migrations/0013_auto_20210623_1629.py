# Generated by Django 3.1.7 on 2021-06-23 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_vehiclestatus_accu_spanning'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vehiclestatus',
            name='accu_spanning',
        ),
        migrations.RemoveField(
            model_name='vehiclestatus',
            name='airco',
        ),
        migrations.RemoveField(
            model_name='vehiclestatus',
            name='batterij_gemiddeld',
        ),
        migrations.RemoveField(
            model_name='vehiclestatus',
            name='error',
        ),
        migrations.RemoveField(
            model_name='vehiclestatus',
            name='trilling',
        ),
        migrations.RemoveField(
            model_name='vehiclestatus',
            name='verwarming',
        ),
        migrations.AddField(
            model_name='vehiclestatus',
            name='aantal_satellieten',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vehiclestatus',
            name='airco_aan',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vehiclestatus',
            name='airco_actief',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vehiclestatus',
            name='baterij_temp',
            field=models.BooleanField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vehiclestatus',
            name='batterij_span_hoog',
            field=models.BooleanField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vehiclestatus',
            name='batterij_span_laag',
            field=models.BooleanField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vehiclestatus',
            name='batterijspanning_gemiddeld',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vehiclestatus',
            name='batterijspanning_maximum',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vehiclestatus',
            name='batterijspanning_minimum',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vehiclestatus',
            name='bedrijfstijd',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vehiclestatus',
            name='controller_temperatuur_alarm',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vehiclestatus',
            name='error_12v',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vehiclestatus',
            name='error_g',
            field=models.BooleanField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vehiclestatus',
            name='gemiddeld_verbruik',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vehiclestatus',
            name='hoogspanningserror',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vehiclestatus',
            name='kabine_ingestelde_temperatuur',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vehiclestatus',
            name='kabine_temperatuur',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vehiclestatus',
            name='motor_temperatuur_alarm',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vehiclestatus',
            name='olie_temperatuur',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vehiclestatus',
            name='spanning_12v',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vehiclestatus',
            name='tanken',
            field=models.BooleanField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vehiclestatus',
            name='versnelling_x_richting',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vehiclestatus',
            name='versnelling_y_richting',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vehiclestatus',
            name='versnelling_z_richting',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='vehiclestatus',
            name='actieradius',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='vehiclestatus',
            name='batterij_percentage',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='vehiclestatus',
            name='batterij_temperatuur',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='vehiclestatus',
            name='controller_temperatuur',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='vehiclestatus',
            name='laden',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='vehiclestatus',
            name='motor_temperatuur',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='vehiclestatus',
            name='snelheid',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='vehiclestatus',
            name='vermogen',
            field=models.IntegerField(),
        ),
    ]