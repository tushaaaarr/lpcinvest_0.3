# Generated by Django 3.1.7 on 2023-01-02 07:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0023_auto_20230102_1320'),
    ]

    operations = [
        migrations.AlterField(
            model_name='constructionupdates',
            name='pub_date',
            field=models.DateField(default=datetime.datetime(2023, 1, 2, 13, 23, 34, 95783)),
        ),
        migrations.AlterField(
            model_name='properties',
            name='pub_date',
            field=models.DateField(default=datetime.datetime(2023, 1, 2, 13, 23, 34, 76899)),
        ),
        migrations.AlterField(
            model_name='teammembers',
            name='email',
            field=models.CharField(blank=True, max_length=40),
        ),
    ]