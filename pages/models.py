from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField

class Page(models.Model):
    title = models.CharField("Título", max_length=200)        # CharField 1
    slug = models.SlugField(unique=True)
    excerpt = models.CharField("Resumen", max_length=250, blank=True)  # CharField 2
    body = RichTextField("Contenido")                          # texto enriquecido
    image = models.ImageField("Imagen", upload_to="pages/", blank=True, null=True)  # imagen
    created = models.DateTimeField("Creado", default=timezone.now)                  # fecha

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.title

# Create your models here.
