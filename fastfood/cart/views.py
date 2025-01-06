from django.shortcuts import render,HttpResponseRedirect
from.models import CartProduct
from.models import FoodList
from.forms import OrderForm,Order
import uuid
import razorpay
from django.views.decorators.csrf import csrf_exempt



# Create your views here.   
def add_to_cart(request,product_id):
    print("product_id",product_id)
    # print("quantity",quantity)
    
    # product = get_object_or_404(FoodList,id=product_id)
    # print("Product NAme>>> ",product.product_name)
    product = FoodList.objects.all().filter(id = product_id).first()

    created = CartProduct.objects.all().filter(productref = product_id).first()
    if created:
        print("created.quantity >>> ",created.quantity)
        created.quantity +=1
        created.save()
    else:
        print("created.NEW >>> ")
        CartProduct.objects.create(
            productref = product,
            quantity = 1,
        )

    print(cart,created)
    return HttpResponseRedirect("/")



def cart(request):
    # CartItem,created=CartItem.objects.get_or_create(CartProduct.request)
    cartitems=CartProduct.objects.all()
    total=0
    for cartitem in cartitems:
        total+=cartitem.quantity*cartitem.productref.product_price
    # print ('Cartitems:',cartitems.productref)
    return render(request,"cart.html",{"cartitems":cartitems,"total":total})


def update_cart(request,cartItem):
    quantity=request.GET.get("quantity")
    cartitem=CartProduct.objects.get(id=cartItem)
    cartitem.quantity=quantity
    cartitem.save()
    return HttpResponseRedirect("/cart")


def checkout(request):
    if request.method=="GET":
        data={"first_name":request.user.first_name,"last_name":request.user.last_name}
        form=OrderForm(initial=data)
        return render(request,"checkout.html",{"form":form})
    if request.method=="POST":
        form=OrderForm(request.POST)
        if form.is_valid():
            order=Order.objects.create(order_id=uuid.uuid4().hex,user=request.user,
                                 first_name=form.cleaned_data["first_name"],
                                 last_name=form.cleaned_data["last_name"],
                                 phoneno=form.cleaned_data["phoneno"],
                                 address_line1=form.cleaned_data["address_line1"],
                                 address_line2=form.cleaned_data["address_line2"],
                                 city=form.cleaned_data["city"],
                                 state=form.cleaned_data["state"],
                                 pincode=form.cleaned_data["pincode"])
            cart=CartProduct.objects.get(id=request.session.get("cart_id"))
            for cartitem in cart.cartitem_set.all():
                cartitem.objects.create(order=order,
                                         product=cartitem.product,
                                         quantity=cartitem.quantity)
            return HttpResponseRedirect("/cart/payment"+order.order_id)

    
@csrf_exempt
def payment(request,totalamount):
   
    amount = totalamount*100
    print(amount)
    

    client=razorpay.Client(auth=("rzp_test_vUuRGMVovGGIMN","0ANDRfXioZ3rCUGQA0z8SR5N"))
    data={"amount": amount,"currency":"INR","receipt":"dhd"}
    payment=client.order.create(data=data)
    print(payment)
    return render(request,"payment.html",{"payment":payment})


@csrf_exempt
def remove_from_cart(request,cartItemId):
    cartitem=CartProduct.objects.get(id=cartItemId)
    cartitem.delete()
    return HttpResponseRedirect("/cart")
