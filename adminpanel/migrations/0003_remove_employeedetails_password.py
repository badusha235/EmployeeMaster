# Generated by Django 3.2.5 on 2021-10-10 03:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adminpanel', '0002_remove_employeedetails_work_location'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employeedetails',
            name='password',
        ),
    ]