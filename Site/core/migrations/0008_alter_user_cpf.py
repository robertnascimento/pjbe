# Generated by Django 4.1 on 2022-08-30 19:50

import cpf_field.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_alter_carro_combustivelcarro_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='cpf',
            field=cpf_field.models.CPFField(max_length=14, verbose_name='cpf'),
        ),
    ]
