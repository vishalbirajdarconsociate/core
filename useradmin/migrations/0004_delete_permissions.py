# Generated by Django 4.1 on 2023-02-03 07:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('useradmin', '0003_alter_permissions_module'),
    ]

    operations = [
        migrations.DeleteModel(
            name='permissions',
        ),
    ]