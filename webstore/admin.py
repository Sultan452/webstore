from django.contrib import admin
from .models import Category, Brand, Product

class CategoryAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]

class BrandAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]

class ProductAdmin(admin.ModelAdmin):
    list_display = ["id", "name","category","brand","price","price","quantity","upload_at"]
    list_filter = ["category", "brand","price","upload_at"]
    search_fields = ["name","brand","category"]
    readonly_fields = ["id","upload_at"]

admin.site.register(Category, CategoryAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(Product, ProductAdmin)

