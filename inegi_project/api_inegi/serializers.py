# api_inegi/serializers.py
from rest_framework import serializers
from .models import Estado, Municipio, Localidad, Asentamiento

class AsentamientoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asentamiento
        fields = ['cve_asen', 'nombre', 'tipo_asen']

class LocalidadSerializer(serializers.ModelSerializer):
    asentamientos = AsentamientoSerializer(many=True, read_only=True)

    class Meta:
        model = Localidad
        fields = [
            'cve_loc', 'nombre', 'latitud', 'longitud', 
            'altitud', 'pob_total', 'total_viviendas_habitadas', 
            'asentamientos'
        ]

class MunicipioSerializer(serializers.ModelSerializer):
    localidades = LocalidadSerializer(many=True, read_only=True)

    class Meta:
        model = Municipio
        fields = ['cve_mun', 'nombre', 'localidades']

class EstadoSerializer(serializers.ModelSerializer):
    municipios = MunicipioSerializer(many=True, read_only=True)

    class Meta:
        model = Estado
        fields = [
            'cve_ent', 'nombre', 'nombre_abrev', 'pob_total', 
            'pob_femenina', 'pob_masculina', 'total_viviendas_habitadas', 
            'municipios'
        ]
