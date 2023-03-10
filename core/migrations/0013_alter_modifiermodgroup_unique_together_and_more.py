# Generated by Django 4.1 on 2023-03-10 06:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_alter_productcategory_unique_together'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='modifiermodgroup',
            unique_together={('modifier', 'modifierGroup')},
        ),
        migrations.AlterUniqueTogether(
            name='productmodgroup',
            unique_together={('product', 'modifierGroup')},
        ),
    ]
