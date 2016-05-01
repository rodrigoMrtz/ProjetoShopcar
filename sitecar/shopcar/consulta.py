#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-
from shopcar.models import Veiculo, Marca, Opcionais, VeiculoOpcionais

class Consulta:

    def pesquisa_marca(self, nome_marca):
        m = Marca.objects.filter(nome=nome_marca)
        return Veiculo.objects.filter(marca=m)

    def pesquisa_modelo(self, nome_modelo):
        return Veiculo.objects.filter(modelo__icontains = nome_modelo)

