# Generated by Django 4.1 on 2022-08-23 10:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('selfstudy', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ev_halkı',
            name='birth_year',
            field=models.IntegerField(blank=True, default=datetime.date(2022, 8, 23), verbose_name='Doğum yılı'),
        ),
    ]
