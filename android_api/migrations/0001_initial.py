# Generated by Django 2.0.4 on 2018-04-12 18:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sensor_Data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temp', models.FloatField()),
                ('pulse', models.IntegerField()),
                ('timestamp', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='User_Info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=40, unique=True)),
                ('password', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('name', models.CharField(max_length=50)),
                ('dob', models.DateField(max_length=8)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(max_length=6)),
                ('bloodgrp', models.CharField(max_length=3)),
                ('city', models.CharField(max_length=40)),
                ('phone', models.IntegerField(max_length=17)),
                ('doctor', models.IntegerField()),
                ('service', models.IntegerField(max_length=1)),
            ],
        ),
        migrations.AddField(
            model_name='sensor_data',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='android_api.User_Info'),
        ),
    ]
