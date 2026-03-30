from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation


class Comentario(models.Model):
    texto = models.TextField(max_length=500) # sql varchar(500)
    autor = models.CharField(max_length=100) # sql varchar(100)
    fecha_creacion = models.DateTimeField(auto_now_add=True) # sql timestamp

    #* A continuacion lo relacionado con ContentType
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    #* Fin de lo concerniente a ContentType

    class Meta: 
        verbose_name = 'Comentario'
        verbose_name_plural = 'Comentarios'
        ordering = ['-fecha_creacion'] # Ordenar por fecha de creación descendente

    def __str__(self):
        return f"Comentario ID: {self.id} -> {self.content_type} ({self.object_id})"
    
class Producto(models.Model):
    nombre = models.CharField(max_length=100) # sql varchar(100)
    precio = models.DecimalField(max_digits=10, decimal_places=2) # sql decimal(10,2)
    descripcion = models.TextField(max_length=1000) # sql varchar(1000)

    #* a continuar lo relacionado con content type
    # consulta inversa o (reverse lookup)
    comentarios = GenericRelation(Comentario)
    # Select * from comentarios where content_type_id = <id de producto> and object_id = <id del producto especifico>
    #* Fin de lo relacionado con content type
    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
    
    def __str__(self):
        return self.nombre
    
class ArticuloBlog(models.Model):
    titulo = models.CharField(max_length=200) # sql varchar(200)
    contenido = models.TextField() # sql text

    #* a continuar lo relacionado con content type
    # consulta inversa o (reverse lookup)
    comentarios = GenericRelation(Comentario)
    #* Fin de lo relacionado con content type

    class Meta:
        verbose_name = 'Artículo de Blog'
        verbose_name_plural = 'Artículos de Blog'
    
    def __str__(self):
        return self.titulo