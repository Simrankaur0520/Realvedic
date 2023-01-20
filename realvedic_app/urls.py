from django.contrib import admin
from django.urls import path
import realvedic_app.views as views 

urlpatterns = [
    path("write_data",views.write_data,name="write_data"),
    path("category_tab_view",views.category_tab_view,name="category_tab_view")
    
    
]