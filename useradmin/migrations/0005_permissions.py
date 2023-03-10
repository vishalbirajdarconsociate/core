# Generated by Django 4.1 on 2023-02-03 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('useradmin', '0004_delete_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='permissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('module', models.ManyToManyField(blank=True, null=True, to='useradmin.modules')),
                ('user', models.ManyToManyField(to='useradmin.logs')),
            ],
        ),
    ]
