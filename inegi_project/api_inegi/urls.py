from django.urls import path
from .views import (
    EstadoListView, MunicipioListView, LocalidadListView, AsentamientoListView,
)
from .export_views import (
    ExportEstadosView, ExportMunicipiosView, ExportLocalidadesView, ExportAsentamientosView
)

urlpatterns = [
    path('estados/', EstadoListView.as_view(), name='estados-list'),
    path('municipios/', MunicipioListView.as_view(), name='municipios-list'),
    path('localidades/', LocalidadListView.as_view(), name='localidades-list'),
    path('asentamientos/', AsentamientoListView.as_view(), name='asentamientos-list'),

    # Rutas de exportación a CSV o Excel
    path('export/estados/', ExportEstadosView.as_view(), name='export-estados'),
    path('export/municipios/', ExportMunicipiosView.as_view(), name='export-municipios'),
    path('export/localidades/', ExportLocalidadesView.as_view(), name='export-localidades'),
    path('export/asentamientos/', ExportAsentamientosView.as_view(), name='export-asentamientos'),
]
