import requests
from .models import Estado, Municipio, Localidad, Asentamiento

def obtener_estados():
    url = "https://gaia.inegi.org.mx/wscatgeo/v2/mgee/"
    try:
        response = requests.get(url)
        response.raise_for_status()
        datos = response.json().get('datos', [])

        if not datos:
            print("No se encontraron datos de estados en la respuesta.")
            return

        for estado in datos:
            Estado.objects.update_or_create(
                cve_ent=estado['cve_ent'],
                defaults={
                    'nombre': estado['nomgeo'],
                    'nombre_abrev': estado['nom_abrev'],
                    'pob_total': estado['pob_total'],
                    'pob_femenina': estado['pob_femenina'],
                    'pob_masculina': estado['pob_masculina'],
                    'total_viviendas_habitadas': estado['total_viviendas_habitadas']
                }
            )
        print("Datos de los estados actualizados correctamente.")
    except requests.exceptions.RequestException as e:
        print(f"Error al realizar la solicitud: {e}")

def obtener_municipios(cve_ent):
    url = f"https://gaia.inegi.org.mx/wscatgeo/v2/mgem/{cve_ent}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        datos = response.json().get('datos', [])

        if not datos:
            print(f"No se encontraron datos de municipios para el estado {cve_ent}.")
            return

        estado = Estado.objects.get(cve_ent=cve_ent)
        for municipio in datos:
            Municipio.objects.update_or_create(
                cve_mun=municipio['cve_mun'],
                estado=estado,
                defaults={
                    'nombre': municipio['nomgeo']
                }
            )
        print(f"Datos de municipios del estado {cve_ent} actualizados correctamente.")
    except requests.exceptions.RequestException as e:
        print(f"Error al realizar la solicitud: {e}")
    except Estado.DoesNotExist:
        print(f"El estado con clave {cve_ent} no existe en la base de datos.")

def obtener_localidades(cve_ent, cve_mun):
    url = f"https://gaia.inegi.org.mx/wscatgeo/v2/localidades/{cve_ent}/{cve_mun}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        datos = response.json().get('datos', [])

        if not datos:
            print(f"No se encontraron datos de localidades para el municipio {cve_mun} del estado {cve_ent}.")
            return

        municipio = Municipio.objects.get(cve_mun=cve_mun, estado__cve_ent=cve_ent)
        for localidad in datos:
            Localidad.objects.update_or_create(
                cve_loc=localidad['cve_loc'],
                municipio=municipio,
                defaults={
                    'nombre': localidad['nomgeo'],
                    'latitud': localidad.get('latitud'),
                    'longitud': localidad.get('longitud'),
                    'altitud': localidad.get('altitud'),
                    'pob_total': localidad.get('pob_total'),
                    'total_viviendas_habitadas': localidad.get('total_viviendas_habitadas')
                }
            )
        print(f"Datos de localidades del municipio {cve_mun} del estado {cve_ent} actualizados correctamente.")
    except requests.exceptions.RequestException as e:
        print(f"Error al realizar la solicitud: {e}")
    except Municipio.DoesNotExist:
        print(f"El municipio con clave {cve_mun} del estado {cve_ent} no existe en la base de datos.")

def obtener_asentamientos(cve_ent, cve_mun):
    url = f"https://gaia.inegi.org.mx/wscatgeo/v2/asentamientos/{cve_ent}/{cve_mun}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        datos = response.json().get('datos', [])

        if not datos:
            print(f"No se encontraron datos de asentamientos para el municipio {cve_mun} del estado {cve_ent}.")
            return

        municipio = Municipio.objects.get(cve_mun=cve_mun, estado__cve_ent=cve_ent)
        for asentamiento in datos:
            try:
                localidad = Localidad.objects.get(
                    cve_loc=asentamiento['cve_loc'],
                    municipio=municipio
                )
                Asentamiento.objects.update_or_create(
                    cve_asen=asentamiento['cve_asen'],
                    localidad=localidad,
                    defaults={
                        'nombre': asentamiento['nom_asen'],
                        'tipo_asen': asentamiento.get('tipo_asen', '')
                    }
                )
            except Localidad.DoesNotExist:
                print(f"La localidad con clave {asentamiento['cve_loc']} en el municipio {cve_mun} no existe.")
        
        print(f"Datos de asentamientos del municipio {cve_mun} del estado {cve_ent} actualizados correctamente.")
    except requests.exceptions.RequestException as e:
        print(f"Error al realizar la solicitud: {e}")
    except Municipio.DoesNotExist:
        print(f"El municipio con clave {cve_mun} del estado {cve_ent} no existe en la base de datos.")
