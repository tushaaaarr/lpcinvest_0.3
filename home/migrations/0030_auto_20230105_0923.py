# Generated by Django 3.1.7 on 2023-01-05 03:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0029_auto_20230103_1056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='constructionupdates',
            name='pub_date',
            field=models.DateField(default=datetime.datetime(2023, 1, 5, 9, 23, 6, 999288)),
        ),
        migrations.AlterField(
            model_name='featuremaster',
            name='feature',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='properties',
            name='pub_date',
            field=models.DateField(default=datetime.datetime(2023, 1, 5, 9, 23, 6, 946162)),
        ),
    ]
