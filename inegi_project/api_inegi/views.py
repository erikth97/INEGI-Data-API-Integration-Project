from django.shortcuts import render

# api_inegi/views.py
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import Estado, Municipio, Localidad, Asentamiento
from .serializers import EstadoSerializer, MunicipioSerializer, LocalidadSerializer, AsentamientoSerializer

class EstadoListView(generics.ListAPIView):
    serializer_class = EstadoSerializer

    def get_queryset(self):
        queryset = Estado.objects.all()

        # Aplicar filtros opcionales
        cve_ent = self.request.query_params.get('cve_ent')
        if cve_ent:
            queryset = queryset.filter(cve_ent=cve_ent)
        
        return queryset

class MunicipioListView(generics.ListAPIView):
    serializer_class = MunicipioSerializer

    def get_queryset(self):
        queryset = Municipio.objects.all()

        # Filtrar por clave de estado si está presente
        cve_ent = self.request.query_params.get('cve_ent')
        if cve_ent:
            queryset = queryset.filter(estado__cve_ent=cve_ent)

        return queryset

class LocalidadListView(generics.ListAPIView):
    serializer_class = LocalidadSerializer

    def get_queryset(self):
        queryset = Localidad.objects.all()

        # Filtrar por clave de estado y municipio si están presentes
        cve_ent = self.request.query_params.get('cve_ent')
        cve_mun = self.request.query_params.get('cve_mun')
        if cve_ent:
            queryset = queryset.filter(municipio__estado__cve_ent=cve_ent)
        if cve_mun:
            queryset = queryset.filter(municipio__cve_mun=cve_mun)

        return queryset

class AsentamientoListView(generics.ListAPIView):
    serializer_class = AsentamientoSerializer

    def get_queryset(self):
        queryset = Asentamiento.objects.all()

        # Filtrar por clave de estado, municipio y localidad si están presentes
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

