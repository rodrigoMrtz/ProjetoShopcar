#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-
from scraper import Scraper
import urllib3, lxml.html, hashlib
from datetime import datetime
from models import Veiculo, Marca, Opcionais, VeiculoOpcionais
from consulta import Consulta

def pesquisa(end):
    shop = "www.shopcar.com.br/"
    endereco_xpath = "//*[contains(@class, 'bt-opcoes')]//a[1]/@href"
    numPag = 1
    scraper = Scraper()
    while True:
        pagina_busca = end
        pagina_busca = pagina_busca.replace("pagina=", "pagina="+str(numPag))
        resultados = scraper.pega_lista(pagina_busca, endereco_xpath)
        if len(resultados) != 0 :
            print("_________----------Página " + str(numPag)+"----------____________")
            for resultado in resultados:
                url = shop+resultado.strip()
                salva(url)
        else:
            print("Acabou os veiculos desta categoria.")
            break
        numPag = numPag + 1

def salva(url_veiculo):
    xpath_categoria = "//*[contains(@class, 'categoria')]/a//text()"
    xpath_marca = "//*[contains(@class, 'marca')]/text()"
    xpath_modelo = "//*[contains(@class, 'modelo')]/text()"
    http = urllib3.PoolManager()
    xpath_especs = "//*[@id=\"dados-veiculo\"]/ul[1]/li/span/text()"
    xpath_preco = "//*[@id=\"dados-veiculo\"]/div/span/text()"
    xpath_opcionais = "//*[contains(@class, 'opcionais')]//li/text()"
    scraper = Scraper()
    print("Xpath Categoria...")
    resultados = scraper.pega_lista(url_veiculo, xpath_categoria)
    v = Veiculo
    o = Opcionais
    if(len(resultados) > 0):#se nao possuir categoria
        v.categoria = resultados[0]
    else:
        v.categoria = "Sem Categoria"
    print("Xpath Marca...")
    resultados = scraper.pega_lista(url_veiculo, xpath_marca)
    try:
        m = Marca.objects.create(nome=resultados[0])
        m.save()
    except:
        m = Marca.objects.get(nome=resultados[0])
    print("Xpath modelo...")
    resultados = scraper.pega_lista(url_veiculo, xpath_modelo)
    v.modelo = resultados[0]
    print("Xpath Especificos...")
    resultados = scraper.pega_lista(url_veiculo, xpath_especs)
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
    resultados = scraper.pega_lista(url_veiculo, xpath_preco)
    r = resultados[0].replace("R$ ", "")
    r = r.replace(",00", "")
    print("preco: ", r)
    if "Consulte" in r:
        r = None
        v.preco = r
    else:
        v.preco = r
    marca = Marca.objects.get(nome=m.nome)
    print("Xpath opcionais...")
    resultados = scraper.pega_lista(url_veiculo, xpath_opcionais)
    for resultado in resultados:
        resultado = resultado.encode('utf-8')
        try:
            o = Opcionais.objects.create(nome=resultado)
            o.save()
        except:
            print("")
    v_hash = marca.nome + v.categoria + v.modelo + v.cor + v.ano_modelo + str(v.km) + v.combustivel + str(v.preco) + ''.join(resultados)
    v_hash = hashlib.md5(v_hash.encode('utf-8'))
    obj_hash = str(v_hash.hexdigest())
    try:
        v = Veiculo.objects.create(vei_pk=obj_hash, marca=marca, categoria=v.categoria, modelo=v.modelo, cor=v.cor, ano_modelo=v.ano_modelo, km=v.km, combustivel=v.combustivel, preco=v.preco)
        v.save()
    except:
        print("Veiculo ja existente no BD")
    for resultado in resultados:
        try:
            vop = VeiculoOpcionais.objects.create(veiculo=v, opcionais=Opcionais.objects.get(nome=resultado))
            vop.save()
        except:
            pass
    print("Terminado.")


arq = open("/home/rodrigo/Área de Trabalho/TCC/WebScrap_Python/Marcas.txt", "r")
tempo = open("/home/rodrigo/tempo_shopcar.txt", "w")
inicio = "Inicio: "+ str(datetime.now())
tempo.write(inicio)
tempo.close()
print(datetime.now())
for linha in arq:
    pesquisa(linha.strip())
final = "Final: "+ str(datetime.now())
arq.close()
tempo = open("/home/rodrigo/tempo_shopcar.txt", "r")
texto = tempo.readlines()
texto.append(final)
tempo = open("/home/rodrigo/tempo_shopcar.txt", "w")
tempo.writelines(texto)
tempo.close()
print("Fim do processo: ",final )
