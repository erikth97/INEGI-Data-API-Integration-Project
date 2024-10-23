from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse  # Importa HttpResponse para devolver una respuesta simple
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

# Define una vista simple para la página de inicio
def home(request):
    return HttpResponse("Welcome to the INEGI API. Visit /api/ for available endpoints.")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api_inegi.urls')),  # Incluye las rutas de la API
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # Endpoint para obtener el token
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # Endpoint para refrescar el token
    path('', home),  # Añade esta línea para manejar la ruta raíz
]
