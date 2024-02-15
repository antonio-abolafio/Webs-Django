from django.contrib import admin
from .models import Product, Category, Tag


# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')


class TagAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')


class ProductAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('name', 'price', 'product_category', 'description', 'product_tag', 'image')
    ordering = ('name', 'categories')
    search_fields = ('name', 'categories', 'tags', 'price')
    date_hierarchy = 'updated'
    list_filter = ('categories', 'tags')

    @staticmethod
    def product_category(obj):
        return ", ".join(category.name for category in obj.categories.all().order_by('name'))

    @staticmethod
    def product_tag(obj):
        return ", ".join(tag.name for tag in obj.tags.all().order_by('name'))


admin.site.register(Tag, TagAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
