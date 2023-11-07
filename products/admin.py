from django.contrib import admin

from products.models import ProductCategory, Product

admin.site.register(ProductCategory)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity', 'category')
    field = ('name', 'description', 'price', 'quantity', 'image', 'category')
    readonly_field = ['description']
    search_fields = ('name',)
    ordering = ('name',)