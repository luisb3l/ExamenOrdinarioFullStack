from django.db import models

class Poema(models.Model):
    CATEGORIAS = [
        ('romantico', 'Romántico'),
        ('tragico', 'Trágico'),
        ('drama', 'Drama')
    ]
    titulo = models.CharField(max_length=255)
    contenido = models.TextField()
    imagen_url = models.URLField()
    categoria = models.CharField(max_length=20, choices=CATEGORIAS)

    def __str__(self):
        return self.titulo