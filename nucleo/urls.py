from django.urls import path
from . import views



app_name = 'nucleo'

urlpatterns = [
    # Feed principal: lista todos los productos y artículos con sus formularios
    path('', views.FeedPrincipalView.as_view(), name='feed_principal'),

    # Detalle de un Producto específico usando su PK (Primary Key) en la URL
    # <int:pk> captura el número de la URL y lo pasa automáticamente a DetailView
    path('producto/<int:pk>/', views.ProductoDetailView.as_view(), name='producto_detail'),

    # Detalle de un Artículo de Blog específico
    path('articulo/<int:pk>/', views.ArticuloDetailView.as_view(), name='articulo_detail'),

    # Vista post-only para procesar comentarios (no tiene template propio)
    path('comentar/', views.AgregarComentarioView.as_view(), name='agregar_comentario'),
]
