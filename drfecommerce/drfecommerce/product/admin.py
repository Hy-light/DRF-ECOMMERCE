from django.contrib import admin

from .models import Category, Brand, Product, ProductLine

# This is the admin interface for the ProductLine model
class ProductLineInline(admin.TabularInline):
    model = ProductLine
    

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductLineInline]

admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(ProductLine)
