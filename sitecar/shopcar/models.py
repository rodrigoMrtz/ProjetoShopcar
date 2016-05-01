from __future__ import unicode_literals

from django.db import models

class Marca(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    def __str__(self):
        return self.nome

class Opcionais(models.Model):
    nome = models.CharField(max_length=30, unique=True)
    def __str__(self):
        return self.nome

class Veiculo(models.Model):
    marca = models.ForeignKey(Marca, null = False)
    opcionais = models.ManyToManyField('Opcionais', through='VeiculoOpcionais')
    categoria = models.CharField(max_length=100, null=True)
    modelo = models.CharField(max_length=100, null=False)
    cor = models.CharField(max_length=50)
    ano_modelo = models.CharField(max_length=10)
    km = models.CharField(max_length=20)
    combustivel = models.CharField(max_length=20)
    preco = models.CharField(max_length=50)

    def __str__(self):
        return self.modelo

class VeiculoOpcionais(models.Model):
    veiculo = models.ForeignKey(Veiculo, null = False)
    opcionais = models.ForeignKey('Opcionais', null = True)