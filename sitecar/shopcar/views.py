from django.shortcuts import render
from .models import Veiculo
from django.views.generic.list import ListView

def index(response):
    veiculos = Veiculo.objects.all()
    return render(response, 'shopcar/index.html', {'veiculos': veiculos})

class ListaVeiculo(ListView):
    template_name = 'shopcar/veiculos/veiculo_list.html'
    model = Veiculo
    paginate_by = 35

    def get_queryset(self):
        v = Veiculo.objects.all()
        q = self.request.GET.get('pesquisar_por')

        # Buscar por veiculo
        if q is not None:
            v = v.filter(modelo__icontains=q)
        return v

    def index(response):
        veiculos = Veiculo.objects.all()
        return render(response, 'shopcar/index.html', {'veiculos': veiculos})