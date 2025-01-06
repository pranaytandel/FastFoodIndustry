from django.db import models
from django.contrib.auth.models import User
from menu.models import FoodList

# Create your models here.

class CartProduct(models.Model):
    productref= models.ForeignKey(FoodList, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    name=models.CharField(max_length=100,default="")

    def __str__(self):
        return self.name
    
class Order(models.Model):
    order_id=models.CharField(primary_key=True,max_length=50)
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    first_name=models.CharField(max_length=100,default="")
    last_name=models.CharField(max_length=100,default="")
    phoneno=models.CharField(max_length=10,default="")
    address_line1=models.TextField(default="")
    address_line2=models.TextField(default="")
    city=models.CharField(max_length=100,default="")
    state=models.CharField(max_length=50,default="")
    pincode=models.IntegerField(default=0)
    created_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)
    paid=models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} - {self.created_at}"
