from django.shortcuts import render_to_response
from django.db.models import Min, Max
from .models import Veiculo, Marca, VeiculoConsulta
from django.views.generic import ListView, TemplateView
from chartit import DataPool, Chart

def graficos(request, param):
    if len(Marca.objects.filter(nome=param)) != 0:
        veiculos = VeiculoConsulta.objects.filter(marca=Marca.objects.get(nome=param)).exclude(preco_min__isnull=True)
    if len(Veiculo.objects.filter(categoria=param)) != 0:
        veiculos = VeiculoConsulta.objects.filter(categoria=param).exclude(preco_min__isnull=True)
    if len(VeiculoConsulta.objects.filter(modelo=param)) != 0:
        veiculos = VeiculoConsulta.objects.filter(modelo=param).exclude(preco_min__isnull=True)
    ds = DataPool(
       series=
        [{'options': {
            'source': veiculos},
          'terms': [
            'ano_modelo',
            'preco_min',
            'preco_max']}
         ])
    cht = Chart(
        datasource = ds, 
        series_options = 
          [{'options':{
              'type': 'line',
              'stacking': False},
            'terms':{
              'ano_modelo': [
                'preco_min',
                'preco_max']
              }}],
        chart_options = 
          {'title': {
               'text': param},
           'xAxis': {
                'title': {
                   'text': 'Ano/Modelo'}}})
    return render_to_response('shopcar/veiculos/graficos.html', {'cht': cht})

def index(request):
    return render_to_response('shopcar/index.html')

class Contato(TemplateView):
    template_name= 'shopcar/contato.html'

class ListaVeiculo(ListView):
    template_name = 'shopcar/veiculos/veiculo_list.html'
    model = Veiculo
    paginate_by = 15

    def get_queryset(self):
        v = Veiculo.objects.values('marca', 'categoria','modelo').annotate(preco_min=Min('preco'), preco_max=Max('preco')).order_by('marca', 'modelo', 'categoria')
        for veiculo in v:
            veiculo['marca'] = Marca.objects.get(id=veiculo['marca'])
        q = self.request.GET.get('pesquisar_por')
        #Buscar por veiculo
        if q is not None:
            v = v.filter(modelo__icontains=q)
            for veiculo in v:
                veiculo['marca'] = Marca.objects.get(id=veiculo['marca'])
        return v