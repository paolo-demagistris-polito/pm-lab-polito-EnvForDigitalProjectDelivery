# Generated by Django 4.0.3 on 2022-05-21 19:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_budget', '0008_contractspending_approval_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contractspending',
            name='date',
            field=models.DateField(default=datetime.date(2022, 5, 21)),
        ),
        migrations.AlterField(
            model_name='resourcespending',
            name='date',
            field=models.DateField(default=datetime.date(2022, 5, 21)),
        ),
    ]
