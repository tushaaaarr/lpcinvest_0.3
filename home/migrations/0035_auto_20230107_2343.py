# Generated by Django 3.1.7 on 2023-01-07 18:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0034_auto_20230107_2334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogs',
            name='pub_date',
            field=models.DateField(default=datetime.datetime(2023, 1, 7, 23, 43, 7, 406886)),
        ),
        migrations.AlterField(
            model_name='constructionupdates',
            name='pub_date',
            field=models.DateField(default=datetime.datetime(2023, 1, 7, 23, 43, 7, 401888)),
        ),
        migrations.AlterField(
            model_name='properties',
            name='deposited_price',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='properties',
            name='pub_date',
            field=models.DateField(default=datetime.datetime(2023, 1, 7, 23, 43, 7, 347221)),
        ),
    ]
