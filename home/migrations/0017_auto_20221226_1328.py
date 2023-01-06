# Generated by Django 3.1.7 on 2022-12-26 07:58

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0016_auto_20221216_1106'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='properties',
            name='area',
        ),
        migrations.AddField(
            model_name='properties',
            name='yields',
            field=models.CharField(blank=True, max_length=40),
        ),
        migrations.AlterField(
            model_name='constructionupdates',
            name='pub_date',
            field=models.DateField(default=datetime.datetime(2022, 12, 26, 13, 28, 1, 532835)),
        ),
        migrations.AlterField(
            model_name='properties',
            name='pub_date',
            field=models.DateField(default=datetime.datetime(2022, 12, 26, 13, 28, 1, 519446)),
        ),
        migrations.CreateModel(
            name='TeamMembers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(blank=True, max_length=30)),
                ('desc', models.TextField(default='')),
                ('mobile', models.CharField(blank=True, max_length=15)),
                ('email', models.CharField(blank=True, max_length=20)),
                ('address', models.CharField(blank=True, max_length=15)),
                ('name', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
