# Autor: Sidney Sousa
import urllib3, lxml.html

class Scraper:

    def pega_lista(self, url, xpath):
        http = urllib3.PoolManager()
        resposta = http.request('GET', url)
        pagina = lxml.html.document_fromstring(resposta.data)
        lista = pagina.xpath(xpath)
        return lista

    def pega_unico(self, url, xpath):
        lista = self.pega_lista(url, xpath)
        return lista[0] if len(lista) > 0 else None

    def gera_histograma(self, url, xpath):
        lista = self.pega_lista(url, xpath)
        histograma = {}
        if len(lista) > 0:
            for chave in lista:
                chave = chave.upper().strip()
                if chave in histograma:
                    histograma[chave] = histograma[chave] + 1
                else:
                    histograma[chave] = 1
        return histograma

