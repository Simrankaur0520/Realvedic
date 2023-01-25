from django.contrib import admin
from django.urls import path
import realvedic_app.views as views 

urlpatterns = [
    path("write_data",views.write_data,name="write_data"),
    path("single_product_view",views.single_product_view,name="single_product_view"),
    path("data_input_pandas",views.data_input_pandas,name="data_input_pandas"),
    
    
    
]