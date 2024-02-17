from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nombre')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')

    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"
        ordering = ["-created"]

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nombre')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "Marca"
        verbose_name_plural = "Marcas"
        ordering = ["-created"]

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nombre')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "Etiqueta"
        verbose_name_plural = "Etiquetas"
        ordering = ["-created"]

    def __str__(self):
        return self.name


# Función para obtener la ruta para guardar la imagen según su categoría y marca
def get_image_upload_path(instance, filename):
    if instance.category:
        category_name = instance.category.name.lower()
        brand_name = instance.brand.name.lower()
        return f'products/{category_name}/{brand_name}/{filename}'
    else:
        return 'products/{filename}'


class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    short_description = models.TextField(null=True, blank=True)
    description = models.TextField()
    image = models.ImageField(upload_to=get_image_upload_path, blank=True, null=True)
    category = models.ForeignKey(Category, null=True, default=None, on_delete=models.CASCADE, verbose_name='Categoría')
    brand = models.ForeignKey(Brand, null=True, default=None, on_delete=models.SET_NULL, verbose_name='Marca')
    tags = models.ManyToManyField(Tag, blank=True, verbose_name='Etiquetas')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"
        ordering = ["-created"]

    def __str__(self):
        return self.name
