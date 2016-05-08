#!/usr/bin/env python
# -*- coding: utf-8 -*-
from scraper import Scraper
import urllib3, lxml.html
from models import Veiculo, Marca, Opcionais, VeiculoOpcionais

xpath_categoria = "//*[contains(@class, 'categoria')]/a//text()"
xpath_marca = "//*[contains(@class, 'marca')]/text()"
xpath_modelo = "//*[contains(@class, 'modelo')]/text()"
url_carro = "http://www.shopcar.com.br/veiculos/ford/fusion-sel-2-5-16v-vvt/08-09/630244"
http = urllib3.PoolManager()
xpath_especs = "//*[@id=\"dados-veiculo\"]/ul[1]/li/span/text()"
xpath_preco = "//*[@id=\"dados-veiculo\"]/div/span/text()"
xpath_opcionais = "//*[contains(@class, 'opcionais')]//li/text()"
scraper = Scraper()
print("Xpath Categoria...")
resultados = scraper.pega_lista(url_carro, xpath_categoria)
v = Veiculo
o = Opcionais
if(len(resultados) > 0):#se nao possuir categoria
    v.categoria = resultados[0]
else:
    v.categoria = "Sem Categoria"
print("Xpath Marca...")
resultados = scraper.pega_lista(url_carro, xpath_marca)
try:
    m = Marca.objects.create(nome=resultados[0])
    m.save()
except:
    print("Nome ja existe no banco carai")
    m = Marca.objects.get(nome=resultados[0])
print("Xpath modelo...")
resultados = scraper.pega_lista(url_carro, xpath_modelo)
print(resultados[0])
v.modelo = resultados[0]
print("Xpath Especificos...")
resultados = scraper.pega_lista(url_carro, xpath_especs)
if (len(resultados) > 3):
    v.ano_modelo = resultados[0]
    v.cor = resultados[1]
    v.km = resultados[2]
    v.combustivel = resultados[3]
elif (len(resultados) == 3):
    v.ano_modelo = resultados[0]
    v.cor = resultados[1]
    v.km = -1
    v.combustivel = resultados[2]
print("Xpath Preco...")
resultados = scraper.pega_lista(url_carro, xpath_preco)
r = resultados[0].replace("R$ ", "")
if "Consulte" in r:
    r = -1
v.preco = r
marca = Marca.objects.get(nome=m.nome)
print("Xpath opcionais...")
resultados = scraper.pega_lista(url_carro, xpath_opcionais)
for resultado in resultados:
    resultado = resultado.encode('utf-8')
    try:
        o = Opcionais.objects.create(nome=resultado)
        o.save()
    except:
        print("opcional existente, proximo")
    print(resultado.strip())

v = Veiculo.objects.create(marca=marca, categoria=v.categoria, modelo=v.modelo, cor=v.cor, ano_modelo=v.ano_modelo, km=v.km, combustivel=v.combustivel, preco=v.preco)
v.save()

for resultado in resultados:
    try:
        vop = VeiculoOpcionais.objects.create(veiculo=v, opcionais=Opcionais.objects.get(nome=resultado))
        vop.save()
    except:
        print("Erro na associacao veiculo aos opcionais")
print("Terminado.")