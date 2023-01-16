import numpy as np
import pandas as pd
import time
from datetime import datetime as dt
import datetime
import re
from operator import itemgetter 
import os
import random


#-------------------------Django Modules---------------------------------------------
from django.http import Http404, HttpResponse, JsonResponse,FileResponse
from django.shortcuts import render
from django.db.models import Avg,Count,Case, When, IntegerField,Sum,FloatField,CharField
from django.db.models import F,Func,Q
from django.db.models import Value as V
from django.db.models.functions import Concat,Cast,Substr
from django.contrib.auth.hashers import make_password,check_password
from django.db.models import Min, Max
from django.db.models import Subquery
#----------------------------restAPI--------------------------------------------------
from rest_framework.decorators import parser_classes,api_view
from rest_framework.parsers import MultiPartParser,FormParser
from rest_framework.response import Response

#----------------------------models---------------------------------------------------
from realvedic_app.models import Product_data
#from apiApp.models import user_whishlist,user_data
#from apiApp.models import metal_price,diamond_pricing


#----------------------------extra---------------------------------------------------
import simplejson as json



#Putting data into database
@api_view(['GET'])
def write_data(request,format=None):
    df=pd.read_csv('product_view.csv')
    #df =pd.Dataframe(data)
    
    data= Product_data(
        Product_name = df["name"],
        category = df["category"],
        image = df[""],
        prices = df["price"],
        Sizes = df["sizes"],
        benefits = df["benefits"],
        ingredients= df["ingredients"],
        how_to_use=df["how_to_use"],
        how_we_make_it = df["how_we_make_it"],
        nutrition= df["nutrition_info"],
        Status = "Inactive",
        sibling_product=df["sibling_product"],
        HSN=df["HSN "],
        SKU=df["SKU"]
        category_colour=df["category_colour"]

    )
    data.save()
    obj=Product_data.objects.values()
    return Response(obj)

def category_tab_view(request,format=None):
    try:
        obj=Product_data.objects.values('category','image','catrgory_colour')
        res={}
        tab=[]
        prod_tab={
            "title": obj.category,
            "image": obj.image,
            "color": obj.category_colour,
        }
        tab.append(prod_tab)
        res['tab']:tab
    except:
        res="Something went wrong, Try again"
        return Response(res)

def banner_view(request,fomat=None):
    res={}
    banner=[]
    try:
        #obj
        bann={
            'image':obj.image,
            'title':obj.category
        }
        
        banner.append(bann)
        res['banner']:banner
        return Response(res)

def top_sellers(request,format=None):
    res={}
    top_selling_products=[]
    try:
        #obj=Product_data.objects.values('category','image','catrgory_colour')
        prod={
            "image": obj.image,
            "title": obj.name,
            "weight": obj.weight,
            "price": obj.prices,
    }
    top_selling_products.append(prod)
    res['products']:top_selling_products
    return Response(res)
