from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=200, verbose_name='Título')
    description = models.TextField(verbose_name='Descripcción')
    image = models.ImageField(verbose_name='Imagen', upload_to='projects')
    link = models.URLField(null=True, blank=True, verbose_name='Dirección web')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')

    class Meta:
        verbose_name = 'Proyecto'
        verbose_name_plural = 'Proyectos'
        ordering = ['-created']

    def __str__(self):
        return self.title
