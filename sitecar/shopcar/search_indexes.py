from haystack import indexes
from .models import VeiculoBusca

class VeiculoIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    modelo = indexes.CharField(model_attr='modelo')
    marca = indexes.CharField(model_attr='marca')
    categoria = indexes.CharField(model_attr='categoria')
    preco_min = indexes.CharField(model_attr='preco_min', null=True)
    preco_max = indexes.CharField(model_attr='preco_max', null=True)
    
    def get_model(self):
        return VeiculoBusca

    def index_queryset(self, using=None):
        return self.get_model().objects.all()