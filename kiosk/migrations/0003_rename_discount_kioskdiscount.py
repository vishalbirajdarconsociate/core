# Generated by Django 4.1 on 2023-03-14 08:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kiosk', '0002_discount'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Discount',
            new_name='KioskDiscount',
        ),
    ]
