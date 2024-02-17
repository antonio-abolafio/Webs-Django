from django.contrib import admin
from .models import Product, Category, Brand, Tag


# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')


class BrandAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')


class TagAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')


class ProductAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('name', 'price', 'product_category', 'brand', 'product_tag', 'image')
    ordering = ('name', 'category')
    search_fields = ('name', 'category', 'brand', 'tags', 'price')
    date_hierarchy = 'updated'
    list_filter = ('category', 'tags')

    @staticmethod
    def product_category(obj):
        if obj.category:
            return obj.category.name
        return None

    @staticmethod
    def product_tag(obj):
        return ", ".join(tag.name for tag in obj.tags.all().order_by('name'))


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(Tag, TagAdmin)
