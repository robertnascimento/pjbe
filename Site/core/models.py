from django.db import models
from cpf_field.models import CPFField

class Carro(models.Model):

    COMBUSTIVEL_CHOICES = [
    ('GASOLINA', 'GASOLINA')
  , ('FLEX', 'FLEX')
  ,('DIESEL', 'DIESEL')
]
    tituloCarro = models.CharField('Título', max_length=20)
    precoCarro = models.IntegerField('Preço')
    anoCarro = models.IntegerField('Ano de fabricação')
    marcaCarro = models.CharField('Marca', max_length=20)
    combustivelCarro = models.CharField('Combustível', blank=True, null=True, choices=COMBUSTIVEL_CHOICES, max_length=8)
    tipoCarro = models.CharField('Tipo', max_length=20)
    created_atCarro = models.DateTimeField(auto_now_add=True) 
    updated_atCarro = models.DateTimeField(auto_now=True)

class Moto(models.Model):

    COMBUSTIVEL_CHOICES = [
    ('GASOLINA', 'GASOLINA ')
  , ('FLEX', 'FLEX ')
  ,('DIESEL', 'DIESEL ')
]
    tituloMoto = models.CharField('Título', max_length=20)
    precoMoto = models.IntegerField('Preço')
    anoMoto = models.IntegerField('Ano de fabricação')
    marcaMoto = models.CharField('Marca', max_length=20)
    combustivelMoto = models.CharField('Combustível', blank=True, null=True, choices=COMBUSTIVEL_CHOICES, max_length=8)
    tipoMoto = models.CharField('Tipo', max_length=20)
    created_atMoto = models.DateTimeField(auto_now_add=True)
    updated_atMoto = models.DateTimeField(auto_now=True)

class User(models.Model):
        
    SEX_CHOICES = [
    ('M', 'Masculino')
  , ('F', 'Feminino')
]
    nome = models.CharField('Nome', max_length=255)
    idade = models.IntegerField('Idade')
    cpf = CPFField('cpf')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    sexo = models.CharField('Sexo', blank=True, null=True, choices=SEX_CHOICES, max_length=1)

