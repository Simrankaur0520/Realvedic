from django.contrib import admin
from django.urls import path
import realvedic_app.views as views 

urlpatterns = [
    path("write_data",views.write_data,name="write_data"),
    path("single_product_view",views.single_product_view,name="single_product_view"),
    path("categoryPage",views.categoryPage,name="categoryPage"),
    path("all_product_view",views.all_product_view,name="all_product_view")

    
    
    
]