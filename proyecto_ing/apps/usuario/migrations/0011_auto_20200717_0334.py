# Generated by Django 2.2 on 2020-07-17 03:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0010_auto_20200717_0301'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='usuario',
            options={'permissions': [('permiso_desde_codigo', 'Este es un permiso creado desde código'), ('segundo_permiso_codigo', 'Segundo permiso creado desde codigo')]},
        ),
    ]
