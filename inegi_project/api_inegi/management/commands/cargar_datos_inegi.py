import requests
from django.core.management.base import BaseCommand
from django.db import transaction
from api_inegi.models import Estado, Municipio, Localidad, Asentamiento
from api_inegi.services import obtener_estados, obtener_municipios, obtener_localidades, obtener_asentamientos

class Command(BaseCommand):
    help = 'Carga datos de INEGI a la base de datos'

    def handle(self, *args, **kwargs):
        self.stdout.write('Iniciando la carga de datos de INEGI...')

        try:
            with transaction.atomic():
                self.cargar_estados()
                self.cargar_municipios()
                self.cargar_localidades()
                self.cargar_asentamientos()

            self.stdout.write(self.style.SUCCESS('Carga de datos completada exitosamente.'))
        except Exception as e:
            self.stderr.write(self.style.ERROR(f'Error durante la carga de datos: {e}'))

    def cargar_estados(self):
        self.stdout.write('Obteniendo datos de los estados...')
        obtener_estados()
        self.stdout.write(self.style.SUCCESS('Datos de los estados actualizados.'))

    def cargar_municipios(self):
        self.stdout.write('Obteniendo datos de los municipios...')
        for estado in Estado.objects.all():
            obtener_municipios(estado.cve_ent)
            self.stdout.write(self.style.SUCCESS(f'Datos de municipios del estado {estado.cve_ent} actualizados.'))

    def cargar_localidades(self):
        self.stdout.write('Obteniendo datos de las localidades...')
        for municipio in Municipio.objects.all():
            obtener_localidades(municipio.estado.cve_ent, municipio.cve_mun)
            self.stdout.write(self.style.SUCCESS(f'Datos de localidades del municipio {municipio.cve_mun} del estado {municipio.estado.cve_ent} actualizados.'))

    def cargar_asentamientos(self):
        self.stdout.write('Obteniendo datos de los asentamientos...')
        for municipio in Municipio.objects.all():
            obtener_asentamientos(municipio.estado.cve_ent, municipio.cve_mun)
            self.stdout.write(self.style.SUCCESS(f'Datos de asentamientos del municipio {municipio.cve_mun} del estado {municipio.estado.cve_ent} actualizados.'))
