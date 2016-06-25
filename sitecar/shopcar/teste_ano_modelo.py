import os
import sys
import django

sys.path.append("/home/rodrigo/TCCWeb/sitecar/") #path to your settings file  
os.environ['DJANGO_SETTINGS_MODULE'] = 'sitecar.settings'
django.setup()

from shopcar.models import Veiculo, VeiculoConsulta


vei = VeiculoConsulta.objects.filter(marca=318)


for v in vei[:20]:
    print(v.ano_modelo)
