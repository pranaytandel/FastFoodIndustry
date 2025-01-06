from django.db import models
from autoslug import AutoSlugField

# Create your models here.

class items(models.Model):
    fooditem_name=models.CharField(max_length=70,default="product name")
    fooditem_Ingredient=models.TextField(default="Ingredient")
    fooditem_price=models.PositiveIntegerField(default=0)
    fooditem_picture=models.ImageField(upload_to="products/",default="")
    
    def __str__(self):
         return self.fooditem_name
    
#=======================================================
#burger category
class Category(models.Model):
    category_name=models.CharField(max_length=45,default="")
    category_slug=AutoSlugField(populate_from='category_name',unique=True,default="default_value")

    def __str__(self):
        return self.category_name
     
    
class FoodList(models.Model):
    product_name=models.CharField(max_length=70,default="product title")
    product_Ingredient=models.CharField(max_length=150,default="Ingredient")
    product_price=models.PositiveIntegerField(default=0)
    product_cat_id=models.PositiveIntegerField(default=0)
    product_fav=models.BooleanField(default=False)
    product_picture=models.ImageField(upload_to="products/",default="")
    product_category_Id=models.ForeignKey(Category,on_delete=models.PROTECT,null=True)
    def __str__(self):
        return self.product_name