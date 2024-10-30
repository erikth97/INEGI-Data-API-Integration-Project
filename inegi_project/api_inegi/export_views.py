import pandas as pd
from django.http import HttpResponse
from django.views import View
from .models import Estado, Municipio, Localidad, Asentamiento

# Exportación de Estados
class ExportEstadosView(View):
    def get(self, request, format='csv'):
        estados = Estado.objects.all().values()
        df = pd.DataFrame(estados)

        if format == 'csv':
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="estados.csv"'
            df.to_csv(path_or_buf=response, index=False, encoding='utf-8') 
        elif format == 'excel':
            response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
            response['Content-Disposition'] = 'attachment; filename="estados.xlsx"'
            df.to_excel(response, index=False, engine='openpyxl')

        return response

# Exportación de Municipios
class ExportMunicipiosView(View):
    def get(self, request, format='csv'):
        municipios = Municipio.objects.all().values()
        df = pd.DataFrame(municipios)

        if format == 'csv':
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="municipios.csv"'
            df.to_csv(path_or_buf=response, index=False, encoding='utf-8')  
        elif format == 'excel':
            response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
            response['Content-Disposition'] = 'attachment; filename="municipios.xlsx"'
            df.to_excel(response, index=False, engine='openpyxl')

        return response

# Exportación de Localidades
class ExportLocalidadesView(View):
    def get(self, request, format='csv'):
        localidades = Localidad.objects.all().values()
        df = pd.DataFrame(localidades)

        if format == 'csv':
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="localidades.csv"'
            df.to_csv(path_or_buf=response, index=False, encoding='utf-8')  
        elif format == 'excel':
            response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
            response['Content-Disposition'] = 'attachment; filename="localidades.xlsx"'
            df.to_excel(response, index=False, engine='openpyxl')

        return response

# Exportación de Asentamientos
class ExportAsentamientosView(View):
    def get(self, request, format='csv'):
        asentamientos = Asentamiento.objects.all().values()
        df = pd.DataFrame(asentamientos)

        if format == 'csv':
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="asentamientos.csv"'
            df.to_csv(path_or_buf=response, index=False, encoding='utf-8')  
        elif format == 'excel':
            response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
            response['Content-Disposition'] = 'attachment; filename="asentamientos.xlsx"'
            df.to_excel(response, index=False, engine='openpyxl')

        return response
