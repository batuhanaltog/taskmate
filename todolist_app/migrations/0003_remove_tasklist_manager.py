# Generated by Django 3.2.16 on 2023-04-06 21:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todolist_app', '0002_tasklist_manager'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tasklist',
            name='manager',
        ),
    ]
