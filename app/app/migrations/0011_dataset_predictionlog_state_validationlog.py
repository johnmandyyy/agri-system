# Generated by Django 4.2.2 on 2025-04-06 16:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_sensorvalue'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dataset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('anemometer', models.IntegerField(default=1)),
                ('rainfall', models.IntegerField(default=1)),
                ('humidity', models.IntegerField(default=1)),
                ('is_storm_present', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='PredictionLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_prediction', models.DateTimeField(default=datetime.datetime(2025, 4, 7, 0, 42, 17, 283855))),
                ('anemometer', models.IntegerField(default=1)),
                ('rainfall', models.IntegerField(default=1)),
                ('humidity', models.IntegerField(default=1)),
                ('is_storm_present', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dc_motor', models.BooleanField(default=False)),
                ('dc_motor_seconds', models.IntegerField(default=0)),
                ('adaptive_mode', models.BooleanField(default=False)),
                ('prediction_minutes_interval', models.IntegerField(default=5)),
            ],
        ),
        migrations.CreateModel(
            name='ValidationLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('anemometer', models.IntegerField(default=1)),
                ('rainfall', models.IntegerField(default=1)),
                ('humidity', models.IntegerField(default=1)),
                ('correct_answer', models.BooleanField(default=False)),
                ('predicted_answer', models.BooleanField(default=False)),
            ],
        ),
    ]
