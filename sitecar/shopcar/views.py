from django.shortcuts import render
from .models import Veiculo

def index(response):
    veiculos = Veiculo.objects.all()
    return render(response, 'shopcar/index.html', {'veiculos': veiculos})