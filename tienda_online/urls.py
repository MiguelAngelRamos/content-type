from django.contrib import admin
from django.urls import path, include

# =============================================================================
# URLs RAÍZ DEL PROYECTO (tienda_poly/urls.py)
# =============================================================================
# Este archivo es el punto de entrada central de todas las URLs.
# Desde aquí se despachan las solicitudes hacia las apps correspondientes.

urlpatterns = [
    # Panel de administración de Django (incluido por defecto)
    path('admin/', admin.site.urls),

    # Todas las URLs de la app 'nucleo' se sirven desde la raíz '/'
    # include() delega al urls.py de la app nucleo
    path('', include('nucleo.urls', namespace='nucleo')),
]
