from django.urls import path
from menu.views import itemsListViews
from.views import ItemDetailView, productFavList
from.views import search
from.views import categoryitems, productList,fav_product

urlpatterns=[
    path ("",itemsListViews.as_view(),name="items"),
    path ("product_fav_list/",productFavList,name="product_fav_list"),
    path ("product_list/<int:catid>/",productList,name="product_list"),
    path("<int:pk>",ItemDetailView.as_view(),name="item_detail"),
    path("search/",search,name="search"),
    path("burger-category/",categoryitems, name='burger'),
    path("update-fav/<int:pk>/",fav_product,name="update-fav"),
   
]