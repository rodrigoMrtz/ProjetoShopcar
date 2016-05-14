from django.shortcuts import render
from django.db.models import Min, Max
from .models import Veiculo
from django.views.generic import ListView, TemplateView
from django.shortcuts import render

def index(response):
    veiculos = Veiculo.objects.all()
    return render(response, 'shopcar/index.html', {'veiculos': veiculos})

class ListaVeiculo(ListView):
    template_name = 'shopcar/veiculos/veiculo_list.html'
    model = Veiculo
    paginate_by = 25

    def get_queryset(self):
        #v = Veiculo.objects.all()
        v = Veiculo.objects.values('categoria','modelo').annotate(preco_min=Min('preco'), preco_max=Max('preco'))
        q = self.request.GET.get('pesquisar_por')
        #Buscar por veiculo
        if q is not None:
            v = v.filter(modelo__icontains=q)
        return v