# Generated by Django 4.1 on 2023-02-27 10:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_productmodgroup'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productmodgroup',
            name='modifier',
        ),
        migrations.AddField(
            model_name='productmodgroup',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.product'),
        ),
        migrations.AlterField(
            model_name='productmodgroup',
            name='modifierGroup',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.modifiergroup'),
        ),
        migrations.CreateModel(
            name='ModifierModGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modifier', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.modifier')),
                ('modifierGroup', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.modifiergroup')),
            ],
        ),
    ]
