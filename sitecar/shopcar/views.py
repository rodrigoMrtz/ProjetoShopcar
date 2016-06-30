from django.shortcuts import render_to_response
from .models import Veiculo, Marca, VeiculoConsulta
from django.views.generic import ListView, TemplateView
from chartit import DataPool, Chart
from .forms import VeiculosSearchForm


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
        form = VeiculosSearchForm(self.request.GET)
        v = form.search()
        return v