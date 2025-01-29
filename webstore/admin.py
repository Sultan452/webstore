from django.contrib import admin
from .models import Category, Brand, Product, CartItem, Cart,Order,Payment

class CartItemAdmin(admin.ModelAdmin):
    list_display = [ "product", "quantity"]


class CartAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "items", "total_cost"]

class OrderAdmin(admin.ModelAdmin):
    list_display = ["id","cart","status", "code"]

class PaymentAdmin(admin.ModelAdmin):
    list_display = ["id", "order", "user","amount", "reference_id","status", "time"]

class CategoryAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]

class BrandAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]

class ProductAdmin(admin.ModelAdmin):
    list_display = ["id", "name","category","brand","price","price","quantity","upload_at"]
    list_filter = ["category", "brand","price","upload_at"]
    search_fields = ["name","brand","category"]
    readonly_fields = ["id","upload_at"]


admin.site.register(CartItem,CartItemAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Cart, CartAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(Product, ProductAdmin)

