from rest_framework import generics
from .models import Estado, Municipio, Localidad, Asentamiento
from .serializers import EstadoSerializer, MunicipioSerializer, LocalidadSerializer, AsentamientoSerializer

# Vista para listar los estados, permitiendo filtrar por clave de estado (cve_ent).
class EstadoListView(generics.ListAPIView):
    serializer_class = EstadoSerializer

    def get_queryset(self):
        # Utiliza prefetch_related para mejorar el rendimiento al traer los datos relacionados.
        queryset = Estado.objects.prefetch_related(
            'municipios__localidades__asentamientos'
        ).order_by('nombre')

        # Filtro opcional por cve_ent (clave de estado).
        cve_ent = self.request.query_params.get('cve_ent')
        if cve_ent:
            queryset = queryset.filter(cve_ent=cve_ent)
        
        return queryset

# Vista para listar los municipios, permite filtrar por clave de estado (cve_ent).
class MunicipioListView(generics.ListAPIView):
    serializer_class = MunicipioSerializer

    def get_queryset(self):
        # Utiliza select_related y prefetch_related para optimizar la consulta.
        queryset = Municipio.objects.select_related('estado').prefetch_related(
            'localidades__asentamientos'
        ).order_by('nombre')

        # Filtro opcional por cve_ent (clave de estado).
        cve_ent = self.request.query_params.get('cve_ent')
        if cve_ent:
            queryset = queryset.filter(estado__cve_ent=cve_ent)

        return queryset

# Vista para listar las localidades, con posibilidad de filtrar por cve_ent y cve_mun.
class LocalidadListView(generics.ListAPIView):
    serializer_class = LocalidadSerializer

    def get_queryset(self):
        queryset = Localidad.objects.select_related(
            'municipio__estado'
        ).prefetch_related('asentamientos').order_by('nombre')

        # Filtros opcionales por cve_ent (estado) y cve_mun (municipio).
        cve_ent = self.request.query_params.get('cve_ent')
        cve_mun = self.request.query_params.get('cve_mun')
        if cve_ent:
            queryset = queryset.filter(municipio__estado__cve_ent=cve_ent)
        if cve_mun:
            queryset = queryset.filter(municipio__cve_mun=cve_mun)

        return queryset

# Vista para listar los asentamientos, con filtros por cve_ent, cve_mun y cve_loc.
class AsentamientoListView(generics.ListAPIView):
    serializer_class = AsentamientoSerializer

    def get_queryset(self):
        queryset = Asentamiento.objects.select_related(
            'localidad__municipio__estado'
        ).order_by('nombre')

        # Filtros opcionales para especificar el estado, municipio y localidad.
        cve_ent = self.request.query_params.get('cve_ent')
        cve_mun = self.request.query_params.get('cve_mun')
        cve_loc = self.request.query_params.get('cve_loc')
        if cve_ent:
            queryset = queryset.filter(localidad__municipio__estado__cve_ent=cve_ent)
        if cve_mun:
            queryset = queryset.filter(localidad__municipio__cve_mun=cve_mun)
        if cve_loc:
            queryset = queryset.filter(localidad__cve_loc=cve_loc)

        return queryset
