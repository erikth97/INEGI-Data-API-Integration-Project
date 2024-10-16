import requests
from django.core.management.base import BaseCommand
from django.db import transaction
from api_inegi.models import Estado, Municipio, Localidad, Asentamiento
from api_inegi.services import obtener_estados, obtener_municipios, obtener_localidades, obtener_asentamientos

# Definir una clase de comando personalizado de Django para cargar datos de la API de INEGI a la base de datos.
class Command(BaseCommand):
    help = 'Carga datos de INEGI a la base de datos'

    # Método principal que se ejecuta al llamar al comando.
    def handle(self, *args, **kwargs):
        self.stdout.write('Iniciando la carga de datos de INEGI...')

        try:
            # Utilizar una transacción atómica para asegurar que todos los datos se carguen correctamente.
            with transaction.atomic():
                self.cargar_estados()         
                self.cargar_municipios()      
                self.cargar_localidades()     
                self.cargar_asentamientos()   

            # Mensaje de éxito si todos los datos se cargan correctamente.
            self.stdout.write(self.style.SUCCESS('Carga de datos completada exitosamente.'))
        except Exception as e:
            # Mensaje de error en caso de que ocurra alguna excepción durante el proceso.
            self.stderr.write(self.style.ERROR(f'Error durante la carga de datos: {e}'))

    # Método para cargar los datos de los estados desde la API.
    def cargar_estados(self):
        self.stdout.write('Obteniendo datos de los estados...')
        obtener_estados()  # Llama a la función que obtiene y guarda los estados en la base de datos.
        self.stdout.write(self.style.SUCCESS('Datos de los estados actualizados.'))

    # Método para cargar los datos de los municipios de cada estado.
    def cargar_municipios(self):
        self.stdout.write('Obteniendo datos de los municipios...')
        for estado in Estado.objects.all():
            obtener_municipios(estado.cve_ent)  # Llama a la función para obtener y guardar los municipios del estado actual.
            self.stdout.write(self.style.SUCCESS(f'Datos de municipios del estado {estado.cve_ent} actualizados.'))

    # Método para cargar los datos de las localidades de cada municipio.
    def cargar_localidades(self):
        self.stdout.write('Obteniendo datos de las localidades...')
        for municipio in Municipio.objects.all():
            obtener_localidades(municipio.estado.cve_ent, municipio.cve_mun)  # Llama a la función para obtener y guardar las localidades del municipio actual.
            self.stdout.write(self.style.SUCCESS(f'Datos de localidades del municipio {municipio.cve_mun} del estado {municipio.estado.cve_ent} actualizados.'))

    # Método para cargar los datos de los asentamientos de cada localidad.
    def cargar_asentamientos(self):
        self.stdout.write('Obteniendo datos de los asentamientos...')
        for municipio in Municipio.objects.all():
            obtener_asentamientos(municipio.estado.cve_ent, municipio.cve_mun)  # Llama a la función para obtener y guardar los asentamientos del municipio actual.
            self.stdout.write(self.style.SUCCESS(f'Datos de asentamientos del municipio {municipio.cve_mun} del estado {municipio.estado.cve_ent} actualizados.'))
