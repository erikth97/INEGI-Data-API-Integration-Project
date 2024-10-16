from django.db import models

class Estado(models.Model):
    cve_ent = models.CharField(max_length=2, unique=True, default='00', db_index=True)
    nombre = models.CharField(max_length=100)
    nombre_abrev = models.CharField(max_length=10, blank=True, null=True)
    pob_total = models.CharField(max_length=10, blank=True, null=True)
    pob_femenina = models.CharField(max_length=10, blank=True, null=True)
    pob_masculina = models.CharField(max_length=10, blank=True, null=True)
    total_viviendas_habitadas = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        return self.nombre

class Municipio(models.Model):
    cve_mun = models.CharField(max_length=4, default='0000', db_index=True)
    nombre = models.CharField(max_length=100)
    estado = models.ForeignKey(Estado, related_name='municipios', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nombre} - {self.estado.nombre}"

class Localidad(models.Model):
    cve_loc = models.CharField(max_length=4, default='0000', db_index=True)
    nombre = models.CharField(max_length=100)
    municipio = models.ForeignKey(Municipio, related_name='localidades', on_delete=models.CASCADE)
    latitud = models.CharField(max_length=15, blank=True, null=True)
    longitud = models.CharField(max_length=15, blank=True, null=True)
    altitud = models.CharField(max_length=10, blank=True, null=True)
    pob_total = models.CharField(max_length=10, blank=True, null=True)
    total_viviendas_habitadas = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} - {self.municipio.nombre}"

class Asentamiento(models.Model):
    cve_asen = models.CharField(max_length=4, default='0000', db_index=True)
    nombre = models.CharField(max_length=255)
    tipo_asen = models.CharField(max_length=50, blank=True, null=True)
    localidad = models.ForeignKey(Localidad, related_name='asentamientos', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nombre} - {self.localidad.nombre}"
