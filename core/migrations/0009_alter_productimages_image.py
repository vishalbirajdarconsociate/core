# Generated by Django 4.1 on 2023-03-01 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_alter_productimages_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productimages',
            name='image',
            field=models.ImageField(upload_to='static/images/product_images/<django.db.models.fields.related.ForeignKey>'),
        ),
    ]
