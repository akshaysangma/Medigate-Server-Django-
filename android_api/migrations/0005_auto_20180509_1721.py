# Generated by Django 2.0.4 on 2018-05-09 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('android_api', '0004_doc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_info',
            name='phone',
            field=models.CharField(max_length=20),
        ),
    ]