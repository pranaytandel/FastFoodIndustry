from django.http import HttpResponseRedirect
from django.shortcuts import render,get_object_or_404
from django.views.generic import ListView,DetailView
from menu.models import items, FoodList
# Create your views here.

class itemsListViews(ListView):
    model=items

class ItemDetailView(DetailView):
    model=FoodList
    template_name="menu/item_detail.html"
    context_object_name="items"

   

def item_detail(request, item_id):
    item =get_object_or_404(items,id=item_id)
    return render(request, 'item_detail.html', {'items': item})



#==============================
#search
#==============================
def search(request):
    keyword=request.GET.get("keyword")
    items_list = FoodList.objects.all().filter(product_name__icontains=keyword)
    return render (request,"menu/search.html",{"items_list":items_list})


#=============================================
def categoryitems(request):
   # burgers=items.objects.filter(category="burger")
    return render(request,"category/category.html")#{"categoryitems":burgers})

def productList(request, catid):
    print('catId',catid)
    items_list = FoodList.objects.all().filter(product_cat_id = catid)
    return render (request,"category/category.html",{"items_list":items_list})

def productFavList(request):
    items_list = FoodList.objects.all().filter(product_fav = True)
    return render (request,"category/category.html",{"items_list":items_list})

def fav_product(request, pk):
    #print('productId >>> ',pk)
    favValue = False
    items_list = FoodList.objects.filter(id = pk).first()
    if items_list.product_fav:
        favValue = False
    else:
        favValue = True
    items_list.product_fav = favValue
    items_list.save()
    print('items_list >>>>>>',items_list)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))