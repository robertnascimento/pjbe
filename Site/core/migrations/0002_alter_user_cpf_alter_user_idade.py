# Generated by Django 4.1 on 2022-08-29 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='cpf',
            field=models.IntegerField(max_length=11, verbose_name='CPF'),
        ),
        migrations.AlterField(
            model_name='user',
            name='idade',
            field=models.IntegerField(max_length=2, verbose_name='Idade'),
        ),
    ]
