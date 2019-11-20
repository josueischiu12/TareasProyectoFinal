from django.db import models
from django.conf import settings

# Create your models here.
class Tarea(models.Model):
    """Model definition for Tarea."""
    ESTADO = [
        (1, "Por Hacer"),
        (2, "Haciendo"),
        (3, "Hecho"),
    ]

    # TODO: Define fields here
    titulo = models.CharField(max_length=20)
    descripcion = models.TextField()
    responsable = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    estado = models.SmallIntegerField(default=1, choices=ESTADO)
    fecha_inicial = models.DateTimeField(null=False, auto_now_add=False)
    fecha_final = models.DateTimeField(null=True)

    class Meta:
        """Meta definition for Tarea."""

        verbose_name = 'Tarea'
        verbose_name_plural = 'Tareas'

    def __str__(self):
        """Unicode representation of Tarea."""
        return self.titulo
