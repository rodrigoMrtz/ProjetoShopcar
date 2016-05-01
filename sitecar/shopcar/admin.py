from django.contrib import admin
from .models import Marca, Veiculo, Opcionais, VeiculoOpcionais

class OpcionaisInline(admin.TabularInline):
    model = VeiculoOpcionais

class VeiculoAdmin(admin.ModelAdmin):
    model = Veiculo
    list_display = ['marca', 'modelo', 'categoria']
    list_filer = ['marca', 'modelo']
    search_fields = ['modelo']
    inlines = [OpcionaisInline]
    save_on_top = True


admin.site.register(Marca)
admin.site.register(Opcionais)
admin.site.register(Veiculo, VeiculoAdmin)