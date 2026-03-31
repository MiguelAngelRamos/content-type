from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.contenttypes.models import ContentType
from django.views import View
from django.views.generic import ListView, DetailView
from .models import Comentario, Producto, ArticuloBlog


class FeedPrincipalView(View):

    def get(self, request):  
        productos = Producto.objects.all()
        articulos = ArticuloBlog.objects.all()

        tipo_prod = ContentType.objects.get_for_model(Producto).id
        tipo_art = ContentType.objects.get_for_model(ArticuloBlog).id

        context = {
            'productos': productos,
            'articulos': articulos,
            'tipo_prod': tipo_prod,
            'tipo_art': tipo_art,
        }
        return render(request, 'nucleo/dashboard.html', context)


# -----------------------------------------------------------------------------
# VISTA 2: ProductoDetailView
# -----------------------------------------------------------------------------
class ProductoDetailView(DetailView):

    model = Producto
    template_name = 'nucleo/producto_detail.html'
    context_object_name = 'producto'


    def get_context_data(self, **kwargs):
        # Siempre llamamos al super() para no perder el contexto base de DetailView.
        context = super().get_context_data(**kwargs)

        # Obtenemos el content_type_id del modelo Producto para el formulario de comentarios.
        context['tipo_prod'] = ContentType.objects.get_for_model(Producto).id

  
        context['comentarios'] = self.object.comentarios.all()
        return context


# -----------------------------------------------------------------------------
# VISTA 3: ArticuloDetailView
# -----------------------------------------------------------------------------
class ArticuloDetailView(DetailView):

    model = ArticuloBlog
    template_name = 'nucleo/articulo_detail.html'
    context_object_name = 'articulo'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tipo_art'] = ContentType.objects.get_for_model(ArticuloBlog).id

        context['comentarios'] = self.object.comentarios.all()
        return context


# -----------------------------------------------------------------------------
# VISTA 4: AgregarComentarioView — EL NÚCLEO DEL SISTEMA POLIMÓRFICO
# -----------------------------------------------------------------------------
class AgregarComentarioView(View):


    def get(self, request):

        return redirect('feed_principal') 

    def post(self, request):

        content_type_id = request.POST.get('content_type_id')
        object_id = request.POST.get('object_id')
        texto = request.POST.get('texto', '').strip()
        autor = request.POST.get('autor', 'Anónimo').strip() or 'Anónimo'


        if not content_type_id or not object_id or not texto:
            return redirect(request.META.get('HTTP_REFERER', '/'))


        tipo_modelo = get_object_or_404(ContentType, id=content_type_id)


        ClaseDelModelo = tipo_modelo.model_class()


        get_object_or_404(ClaseDelModelo, id=object_id)

        Comentario.objects.create(
            content_type=tipo_modelo,  # Mandamos la instancia del Metadata Type
            object_id=object_id,       # Mandamos el Integer del Primary Key originado
            texto=texto,               # Cuerpo orgánico del usuario
            autor=autor,
        )

        return redirect(request.META.get('HTTP_REFERER', '/'))
