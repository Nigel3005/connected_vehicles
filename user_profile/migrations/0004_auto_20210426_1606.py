# Generated by Django 3.1.7 on 2021-04-26 14:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0003_auto_20210426_1328'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='test_1',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='test_2',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='vehicle_name',
        ),
    ]
