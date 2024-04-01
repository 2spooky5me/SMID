# Generated by Django 5.0.3 on 2024-03-20 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ubicaciones', '0002_alter_historicallocalidad_local_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicallocalidad',
            name='local',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='historicallocalidad',
            name='type_local',
            field=models.CharField(choices=[('CO', 'Consultorio'), ('OT', 'Otro')], max_length=2, verbose_name='Tipo Local'),
        ),
        migrations.AlterField(
            model_name='localidad',
            name='local',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='localidad',
            name='type_local',
            field=models.CharField(choices=[('CO', 'Consultorio'), ('OT', 'Otro')], max_length=2, verbose_name='Tipo Local'),
        ),
    ]
