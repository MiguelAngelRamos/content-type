from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
# Create your models here.
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