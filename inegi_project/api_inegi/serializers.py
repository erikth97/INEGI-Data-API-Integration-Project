from rest_framework import serializers
from .models import Estado, Municipio, Localidad, Asentamiento

# Serializador para Asentamiento, convierte el modelo Asentamiento a JSON.
class AsentamientoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asentamiento
        fields = ['cve_asen', 'nombre', 'tipo_asen']

# Serializador para Localidad, incluye la lista de asentamientos anidados.
class LocalidadSerializer(serializers.ModelSerializer):
    asentamientos = AsentamientoSerializer(many=True, read_only=True)

    class Meta:
        model = Localidad
        fields = [
            'cve_loc', 'nombre', 'latitud', 'longitud', 
            'altitud', 'pob_total', 'total_viviendas_habitadas', 
            'asentamientos'
        ]

# Serializador para Municipio, incluye la lista de localidades anidadas.
class MunicipioSerializer(serializers.ModelSerializer):
    localidades = LocalidadSerializer(many=True, read_only=True)

    class Meta:
        model = Municipio
        fields = ['cve_mun', 'nombre', 'localidades']

# Serializador para Estado, incluye la lista de municipios anidados.
class EstadoSerializer(serializers.ModelSerializer):
    municipios = MunicipioSerializer(many=True, read_only=True)

    class Meta:
        model = Estado
        fields = [
            'cve_ent', 'nombre', 'nombre_abrev', 'pob_total', 
            'pob_femenina', 'pob_masculina', 'total_viviendas_habitadas', 
            'municipios'
        ]
