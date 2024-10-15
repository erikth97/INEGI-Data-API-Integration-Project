from django.db import models

# Modelo para los Estados
class Estado(models.Model):
    nombre = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Estado"
        verbose_name_plural = "Estados"

    def __str__(self):
        return self.nombre


# Modelo para los Municipios
class Municipio(models.Model):
    nombre = models.CharField(max_length=100)
    estado = models.ForeignKey(Estado, related_name='municipios', on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Municipio"
        verbose_name_plural = "Municipios"

    def __str__(self):
        return self.nombre


# Modelo para las Localidades
class Localidad(models.Model):
    nombre = models.CharField(max_length=100)
    municipio = models.ForeignKey(Municipio, related_name='localidades', on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Localidad"
        verbose_name_plural = "Localidades"

    def __str__(self):
        return self.nombre


# Modelo para los Asentamientos
class Asentamiento(models.Model):
    nombre = models.CharField(max_length=100)
    localidad = models.ForeignKey(Localidad, related_name='asentamientos', on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Asentamiento"
        verbose_name_plural = "Asentamientos"

    def __str__(self):
        return self.nombre
