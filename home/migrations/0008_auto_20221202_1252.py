# Generated by Django 3.1.7 on 2022-12-02 07:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_auto_20221201_2032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='properties',
            name='area',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='properties',
            name='pub_date',
            field=models.DateField(default=datetime.datetime(2022, 12, 2, 12, 52, 35, 429866)),
        ),
    ]
