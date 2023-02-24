# Generated by Django 4.1 on 2023-02-06 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('useradmin', '0008_logs_module'),
    ]

    operations = [
        migrations.CreateModel(
            name='group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_name', models.CharField(max_length=50)),
                ('group_modules', models.ManyToManyField(blank=True, null=True, to='useradmin.modules')),
            ],
        ),
    ]