# Generated by Django 2.2 on 2021-03-27 01:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_1', '0004_auto_20210326_2323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='representante',
            name='id_emp',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app_1.Empresa'),
        ),
    ]
