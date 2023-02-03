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
from realvedic_app.models import user_data,user_address
from realvedic_app.models import Product_data
from realvedic_app.models import user_cart

#----------------------------extra---------------------------------------------------
import simplejson as json

def user_cart_view(request,format=None):
    token = request.data['token']
    try:
        user = user_data.objects.get(token = token)
    except:
        res = {
                'status':False,
                'message':'Something went wrong'
            }
        return Response(res)
    products = Product_data.objects.values()
    items = user_cart.objects.filter(user_id = user.id).values()
    if len(items)==0:
        res = {
            'status':True,
            'message':'Cart generated',
            'products':[],
            'checkout_data': []
          }
        return Response(res)
    #quantity=1
    product_list = []
    final_sub_total = 0
    final_making_charges = 0
    shipping = 100
    tax = 1.8
    for i in items:
        prod_data = products.filter(id = i['product_id']).last()
    
        prod_dict = {
                     'cart_product_id':i['id'],
                     'id':prod_data['id'],
                     'image':prod_data['image'].split(',')[0],
                     'title':prod_data['name'],
                     'quantity':i['quantity']
                    }
    return("in progress")