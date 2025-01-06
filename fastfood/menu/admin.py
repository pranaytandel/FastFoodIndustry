from django.contrib import admin
from.models import items
from .models import Category
from .models import FoodList

class FoodListAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'product_Ingredient', 'product_price', 'product_cat_id', 'product_fav')
    list_filter = ('product_fav', 'product_cat_id')
    search_fields = ('product_name', 'product_Ingredient')

admin.site.register(FoodList, FoodListAdmin)

# Register your models here.

class ItemsAdmin(admin.ModelAdmin):
    list_display=['id','fooditem_name','fooditem_Ingredient','fooditem_price']

admin.site.register(items, ItemsAdmin)


#==================================
class CategoryAdmin(admin.ModelAdmin):
    list_display=["id","category_name","category_slug"]
admin.site.register(Category,CategoryAdmin)

