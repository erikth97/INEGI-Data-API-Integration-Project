from django.urls import path
from .views import EstadoListView, MunicipioListView, LocalidadListView, AsentamientoListView

urlpatterns = [
    path('estados/', EstadoListView.as_view(), name='estados-list'),
    path('municipios/', MunicipioListView.as_view(), name='municipios-list'),
    path('localidades/', LocalidadListView.as_view(), name='localidades-list'),
    path('asentamientos/', AsentamientoListView.as_view(), name='asentamientos-list'),
]
