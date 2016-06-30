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
    vei_pk = models.CharField(max_length=32, unique=True) 
    marca = models.ForeignKey(Marca, null = False)
    opcionais = models.ManyToManyField('Opcionais', through='VeiculoOpcionais')
    categoria = models.CharField(max_length=100, null=True)
    modelo = models.CharField(max_length=100, null=False)
    cor = models.CharField(max_length=50)
    ano_modelo = models.CharField(max_length=10)
    km = models.CharField(max_length=20)
    combustivel = models.CharField(max_length=20)
    preco = models.DecimalField(max_digits=10, decimal_places=3, null=True)

    def __str__(self):
        return self.modelo

class VeiculoOpcionais(models.Model):
    veiculo = models.ForeignKey(Veiculo, null = False)
    opcionais = models.ForeignKey('Opcionais', null = True)

class VeiculoConsulta(models.Model):
    id = models.BigIntegerField(primary_key=True)
    marca = models.ForeignKey(Marca, on_delete=models.DO_NOTHING)
    categoria = models.CharField(max_length=100, null=True)
    modelo = models.CharField(max_length=100, null=False)
    ano_modelo = models.CharField(max_length=10)
    preco_min = models.DecimalField(max_digits=5, decimal_places=3, null=True)
    preco_max = models.DecimalField(max_digits=5, decimal_places=3, null=True)

class Meta:
    managed = False
    db_table= 'shopcar_veiculoconsulta'

class VeiculoBusca(models.Model):
    id = models.BigIntegerField(primary_key=True)
    marca = models.ForeignKey(Marca, on_delete=models.DO_NOTHING)
    categoria = models.CharField(max_length=100, null=True)
    modelo = models.CharField(max_length=100, null=False)
    preco_min = models.DecimalField(max_digits=5, decimal_places=3, null=True)
    preco_max = models.DecimalField(max_digits=5, decimal_places=3, null=True)

class Meta:
    managed = False
    db_table = 'shopcar_veiculobusca'