# Generated by Django 5.0.3 on 2024-04-05 14:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ubicaciones', '0017_alter_localidad_unique_together_and_more'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='localidad',
            unique_together={('tower', 'floor', 'type_local', 'local')},
        ),
    ]
