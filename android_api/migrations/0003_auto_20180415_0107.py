# Generated by Django 2.0.4 on 2018-04-14 19:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('android_api', '0002_auto_20180412_2335'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cont_Pulse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pulsevalue', models.IntegerField()),
                ('timestamp', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='user_info',
            name='id',
        ),
        migrations.AlterField(
            model_name='user_info',
            name='username',
            field=models.CharField(max_length=40, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='cont_pulse',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='android_api.User_Info'),
        ),
    ]