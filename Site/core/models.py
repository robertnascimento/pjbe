from django.db import models

class Carro(models.Model):
    tituloCarro = models.CharField('Título', max_length=20)
    precoCarro = models.IntegerField('Preço')
    anoCarro = models.IntegerField('Ano de fabricação')
    marcaCarro = models.CharField('Marca', max_length=20)
    combustivelCarro = models.CharField('Combustível', max_length=20)
    tipoCarro = models.CharField('Tipo', max_length=20)
    created_atCarro = models.DateTimeField(auto_now_add=True) 
    updated_atCarro = models.DateTimeField(auto_now=True)

class Moto(models.Model):
    tituloMoto = models.CharField('Título', max_length=100)
    precoMoto = models.IntegerField('Preço')
    anoMoto = models.IntegerField('Ano de fabricação')
    marcaMoto = models.CharField('Marca', max_length=20)
    combustivelMoto = models.CharField('Combustível', max_length=20)
    tipoMoto = models.CharField('Tipo', max_length=20)
    created_atMoto = models.DateTimeField(auto_now_add=True)
    updated_atMoto = models.DateTimeField(auto_now=True)

class User(models.Model):
    nome = models.CharField('Nome', max_length=255)
    idade = models.IntegerField('Idade')
    cpf = models.IntegerField('CPF')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
