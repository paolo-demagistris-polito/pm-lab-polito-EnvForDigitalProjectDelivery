# Generated by Django 4.0.3 on 2022-04-19 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_charter', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectcharter',
            name='business_case',
            field=models.CharField(blank=True, max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name='projectcharter',
            name='contract',
            field=models.CharField(blank=True, max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name='projectcharter',
            name='sow',
            field=models.CharField(blank=True, max_length=1024, null=True),
        ),
    ]