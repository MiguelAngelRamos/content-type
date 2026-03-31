from django.shortcuts import render
from django.views import View
from django.views.generic import DetailView
from .models import Producto, ArticuloBlog
from django.contrib.contenttypes.models import ContentType
# El DetailView se utiliza para mostrar los detalles de un solo objeto, mientras que el ListView se utiliza para mostrar una lista de objetos.

class FeedPrincialView(View):
    def get(self, request):
        productos = Producto.objects.all()
        articulos = ArticuloBlog.objects.all()

        #* A continuacion lo relacionado con ContentType
        #* ContentType.objects.get_for_model(Modelo) -> Devuelve el ContentType para un modelo específico

        #* Comentario.objects.filter(content_type=ContentType.objects.get_for_model(Producto)) -> Devuelve todos los comentarios relacionados con el modelo Producto
        #* Comentario.objects.filter(content_type=ContentType.objects.get_for_model(ArticuloBlog)) -> Devuelve todos los comentarios relacionados con el modelo ArticuloBlog

        tipo_producto = ContentType.objects.get_for_model(Producto).id#* Son Ids internos que Django utiliza para identificar el modelo al que se relacionan los comentarios
        tipo_articulo = ContentType.objects.get_for_model(ArticuloBlog).id #* Son Ids internos que Django utiliza para identificar el modelo al que se relacionan los comentarios

        context = {
            'productos': productos,
            'articulos': articulos,
            'tipo_producto': tipo_producto,
            'tipo_articulo': tipo_articulo,
        }
        return render(request, 'nucleo/dashboard.html', context)

# Create your views here.
class ProductoDetailView(DetailView):
    pass


class ArticuloBlogDetailView(DetailView):
    pass