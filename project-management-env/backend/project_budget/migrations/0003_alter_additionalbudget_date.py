# Generated by Django 4.0.3 on 2022-06-18 13:59

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('project_budget', '0002_alter_contractspending_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='additionalbudget',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]