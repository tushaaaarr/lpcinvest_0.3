# Generated by Django 3.1.7 on 2022-12-28 12:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0020_auto_20221228_1727'),
    ]

    operations = [
        migrations.AlterField(
            model_name='constructionupdates',
            name='pub_date',
            field=models.DateField(default=datetime.datetime(2022, 12, 28, 17, 37, 25, 319317)),
        ),
        migrations.AlterField(
            model_name='properties',
            name='pub_date',
            field=models.DateField(default=datetime.datetime(2022, 12, 28, 17, 37, 25, 307324)),
        ),
        migrations.AlterField(
            model_name='teammembers',
            name='address',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
