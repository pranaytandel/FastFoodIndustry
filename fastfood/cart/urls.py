from django.urls import path
from.import views


urlpatterns = [
   path('add-to-cart/<int:product_id>/',views.add_to_cart, name='add_to_cart'),
   path("",views.cart,name="cart"),
   path("update-quantity/<int:cartItem>/",views.update_cart,name="update-quantity"),
   path("checkout/",views.checkout,name="checkout"),
   path("payment/<int:totalamount>/",views.payment,name="payment"),
   path("remove-from-cart/<int:cartItemId>/",views.remove_from_cart,name="remove-from-cart"),
 
  
]
