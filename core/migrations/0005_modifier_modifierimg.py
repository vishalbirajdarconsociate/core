# Generated by Django 4.1 on 2023-02-27 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_remove_productmodgroup_modifier_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='modifier',
            name='modifierImg',
            field=models.ImageField(null=True, upload_to='static/images/modifier_images/'),
        ),
    ]
