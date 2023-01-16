from django.contrib import admin
from django.urls import path
import realvedic_app.views as views 

urlpatterns = [
    path("write_data",views.write_data,name="write_data"),
    
]