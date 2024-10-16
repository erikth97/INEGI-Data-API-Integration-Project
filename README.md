# INEGI Data API Project

## Descripción
Este proyecto permite consultar datos geográficos de México desde la API de INEGI, almacenarlos en una base de datos MySQL y exponer esta información a través de un API REST usando Django y Django Rest Framework. 

## Características
- Conexión a la API de INEGI para obtener información de estados, municipios, localidades y asentamientos.
- Almacenamiento de datos en una base de datos MySQL.
- API REST para consultar la información, con filtros para estados, municipios, localidades y asentamientos.
- Paginación para manejar grandes volúmenes de datos.
- Optimización de consultas a la base de datos para un rendimiento eficiente.

## Requisitos Previos
- Python 3.12
- MySQL 8.0 o superior
- `virtualenv` para crear un entorno virtual
- `mysqlclient` para conectar Django con MySQL

## Instalación
Sigue los pasos a continuación para configurar el proyecto en tu entorno local:

### 1. Clonar el Repositorio
```bash
git clone https://github.com/tu_usuario/inegi_project.git
cd inegi_project
```

### 2. Crear un Entorno Virtual
```bash
python -m venv env
```

### 3. Activar el Entorno Virtual
**Windows:**
```bash
.\env\Scripts\activate
```
**Linux/Mac:**
```bash
source env/bin/activate
```

### 4. Instalar las Dependencias
```bash
pip install -r requirements.txt
```

### 5. Configurar la Base de Datos
Edita el archivo `inegi_project/settings.py` y asegúrate de que la configuración de la base de datos sea correcta:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'inegi_db',
        'USER': 'user',  
        'PASSWORD': 'contraseña', 
        'HOST': 'localhost',  
        'PORT': '3306',  
    }
}
```

### 6. Migraciones de la Base de Datos
Ejecuta las migraciones para crear las tablas en la base de datos:

```bash
python manage.py makemigrations
python manage.py migrate
```

### 7. Poblar la Base de Datos con Datos del INEGI
Ejecuta el comando personalizado para obtener y almacenar los datos de la API de INEGI:

```bash
python manage.py cargar_datos_inegi
```

### 8. Ejecutar el Servidor
Inicia el servidor de desarrollo de Django:

```bash
python manage.py runserver
```

Visita [http://127.0.0.1:8000/api/](http://127.0.0.1:8000/api/) para ver la API en funcionamiento.

## Endpoints Disponibles

- **GET /api/estados/**: Lista todos los estados. Filtros:
  - `cve_ent`: Filtra por clave de estado.
  
- **GET /api/municipios/**: Lista todos los municipios. Filtros:
  - `cve_ent`: Filtra por clave de estado.
  
- **GET /api/localidades/**: Lista todas las localidades. Filtros:
  - `cve_ent`: Filtra por clave de estado.
  - `cve_mun`: Filtra por clave de municipio.
  
- **GET /api/asentamientos/**: Lista todos los asentamientos. Filtros:
  - `cve_ent`: Filtra por clave de estado.
  - `cve_mun`: Filtra por clave de municipio.
  - `cve_loc`: Filtra por clave de localidad.
