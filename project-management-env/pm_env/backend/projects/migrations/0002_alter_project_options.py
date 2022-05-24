# Generated by Django 4.0.3 on 2022-05-21 19:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ('project_name',), 'permissions': (('add_project_charter', 'Can add project charter /to project charter'), ('change_project_charter', 'Can change project charter'), ('delete_project_charter', 'Can delete project charter'), ('view_project_charter', 'Can view project charter'), ('add_project_resource', 'Can add project resource'), ('change_project_resource', 'Can change project resource'), ('delete_project_resource', 'Can delete project resource'), ('view_project_resource', 'Can view project resource'), ('add_project_contract', 'Can add project contract'), ('change_project_contract', 'Can change project contract'), ('delete_project_contract', 'Can delete project contract'), ('view_project_contract', 'Can view project contract'))},
        ),
    ]
