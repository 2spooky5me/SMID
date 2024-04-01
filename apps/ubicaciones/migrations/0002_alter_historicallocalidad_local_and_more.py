# Generated by Django 5.0.3 on 2024-03-20 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ubicaciones', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicallocalidad',
            name='local',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='historicallocalidad',
            name='type_local',
            field=models.CharField(blank=True, choices=[('CO', 'Consultorio'), ('OT', 'Otro')], max_length=2, null=True, verbose_name='Tipo Local'),
        ),
        migrations.AlterField(
            model_name='localidad',
            name='local',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='localidad',
            name='type_local',
            field=models.CharField(blank=True, choices=[('CO', 'Consultorio'), ('OT', 'Otro')], max_length=2, null=True, verbose_name='Tipo Local'),
        ),
    ]
