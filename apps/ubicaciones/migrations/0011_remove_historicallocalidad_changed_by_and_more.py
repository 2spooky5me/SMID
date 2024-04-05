# Generated by Django 5.0.3 on 2024-04-05 09:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ubicaciones', '0010_remove_torre_unique_if_status_not_false_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='historicallocalidad',
            name='changed_by',
        ),
        migrations.RemoveField(
            model_name='historicallocalidad',
            name='floor',
        ),
        migrations.RemoveField(
            model_name='historicallocalidad',
            name='history_user',
        ),
        migrations.RemoveField(
            model_name='historicallocalidad',
            name='tower',
        ),
        migrations.RemoveField(
            model_name='historicalpiso',
            name='changed_by',
        ),
        migrations.RemoveField(
            model_name='historicalpiso',
            name='history_user',
        ),
        migrations.RemoveField(
            model_name='historicaltorre',
            name='changed_by',
        ),
        migrations.RemoveField(
            model_name='historicaltorre',
            name='history_user',
        ),
        migrations.RemoveField(
            model_name='historicalubicacion',
            name='changed_by',
        ),
        migrations.RemoveField(
            model_name='historicalubicacion',
            name='history_user',
        ),
        migrations.RemoveField(
            model_name='historicalubicacion',
            name='location_cpv',
        ),
        migrations.RemoveConstraint(
            model_name='piso',
            name='floor_unique_if_status_not_false',
        ),
        migrations.RemoveConstraint(
            model_name='torre',
            name='tower_unique_if_status_not_false',
        ),
        migrations.AlterField(
            model_name='localidad',
            name='local',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='piso',
            name='name',
            field=models.CharField(max_length=20, unique=True, verbose_name='Nombre'),
        ),
        migrations.AlterField(
            model_name='torre',
            name='name',
            field=models.CharField(max_length=20, unique=True, verbose_name='Nombre'),
        ),
        migrations.AlterField(
            model_name='ubicacion',
            name='location',
            field=models.TextField(blank=True, null=True, unique=True, verbose_name='Direccion'),
        ),
        migrations.AlterField(
            model_name='ubicacion',
            name='location_cpv',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, to='ubicaciones.localidad', unique=True, verbose_name='Localidad CPV'),
        ),
        migrations.DeleteModel(
            name='HistoricalLocalidad',
        ),
        migrations.DeleteModel(
            name='HistoricalPiso',
        ),
        migrations.DeleteModel(
            name='HistoricalTorre',
        ),
        migrations.DeleteModel(
            name='HistoricalUbicacion',
        ),
    ]
