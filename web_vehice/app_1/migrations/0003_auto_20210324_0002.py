# Generated by Django 2.2 on 2021-03-24 00:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_1', '0002_auto_20210323_2331'),
    ]

    operations = [
        migrations.RenameField(
            model_name='representante',
            old_name='dir_centro',
            new_name='ciudad_centro',
        ),
        migrations.AddField(
            model_name='empresa',
            name='choice',
            field=models.CharField(choices=[('XV', 'Región de Arica y Parinacota'), ('I', 'Región de Tarapacá'), ('II', 'Región de Antofagasta'), ('III', 'Región de Atacama'), ('IV', 'Región de Coquimbo'), ('V', 'Región de Valparaíso'), ('RM', 'Región Metropolitana de Santiago'), ('VI', 'Región del Libertador General Bernardo OHiggins'), ('VII', 'Región del Maule'), ('XVI', 'Región del Ñuble'), ('VIII', 'Región del Biobío'), ('IX', 'Región de La Araucania'), ('XIV', 'Región de Los Ríos'), ('X', 'Región de Los Lagos'), ('XI', 'Región de Aysén del General Carlos Ibáñez del Campo'), ('XII', 'Región de Magallanes y la Antártica Chilena')], default='', max_length=4),
        ),
    ]
