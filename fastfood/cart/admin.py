from django.contrib import admin
from .models import  CartProduct,Order
# Register your models here.
class CartProductAdmin(admin.ModelAdmin):
    list_display=['id','productref','quantity']

admin.site.register(CartProduct, CartProductAdmin)
admin.site.register(Order)
