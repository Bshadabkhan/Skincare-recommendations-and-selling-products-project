from django.urls import path,include
from .views import *

urlpatterns = [
    path("filter/",product_list),
    path('',filter_products, name='filter_products'),
    path('product/',product, name="product"),
    path('index',index,name="index")

]
