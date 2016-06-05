import datetime
from haystack import indexes
from shopcar.models import Veiculo

class VeiculoIndex(indexes.SearchIndex, indexes.Indexable):
    texto_modelo = indexes.CharField(document=True, model_attr='modelo')
    
    def get_model(self):
        return Veiculo
