from django.contrib import admin
from import_export import resources
from Planilla.models import Planilla

# Register your models here.
class PlanillaResource(resources.ModelResource):

    class Meta:
        model = Planilla

class PlanillaAdmin (admin.ModelAdmin):
    resources_class = PlanillaResource
    # con esto muestras los campos que deses al mostrar la lista en admin
    list_display= ['Dia','Propietario','Manzana','Lote','cant','Aprobado']
    # con esto añades un campo de texto que te permite realizar la busqueda, puedes añadir mas de un atributo por el cual se filtrará
    search_fields = ['Propietario']
    list_filter = ['Dia']

admin.site.register(Planilla,PlanillaAdmin)
