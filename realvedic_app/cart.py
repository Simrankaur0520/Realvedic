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

#---------------------------------------------------------------------------------------------------------------------------------
##################################################################################################################################
#------------------------------------------------Add To cart----------------------------------------------------------------------
#*********************************************************************************************************************************
''' user_id = models.TextField()
    product_id = models.TextField()
    size = models.TextField()
    price_per_unit=models.TextField()
    quantity = models.TextField(blank=True)
    updated_at = models.DateTimeField(auto_now=True)'''
 
@api_view(['POST'])
def add_to_cart(request,fromat=None):
     if request.method == 'POST':
        token = request.data['token']
        product_id = request.data['product_id']
        size = request.data['size']
        price=request.data['price']
        
        #----------------Checking for Product id in produt data

        try:
            Product_data.objects.get(id=product_id)
            print("1st try encounetred")
            try:
                user = user_data.objects.get(token = token)
                print("2nd try encounetred")
            except:
                res = {
                        'status':False,
                        'message':'Something went wrong'
                    }
                return Response(res)
            obj = user_cart.objects.filter(user_id = user.id,
                                        product_id = product_id,
                                        price_per_unit=price,
                                        size = size
                                        ).values()
            if len(obj) == 0:
                data = user_cart(
                                    user_id = user.id,
                                    product_id = product_id,
                                    size = size,
                                    price_per_unit=price,
                                    quantity = '1',
              
                                )
                data.save()
               
                res = {
                        
                        'status' : True,
                        'message': 'Product added to cart successfully'
                    }
                return Response(res)
            else:
                obj = user_cart.objects.filter(user_id = user.id,
                                        product_id = product_id,
                                        size = size,
                                        price_per_unit=price).values().last()
                quantity = int(obj['quantity'])+1
                user_cart.objects.filter(user_id = user.id,
                                        product_id = product_id,
                                        size = size,
                                        price_per_unit=price,
                                       ).update(quantity = quantity)
                res = {
                        'status' : True,
                        'message': 'Product already exist, quantity increased'
                    }
                return Response(res)
                    

        #---------------Except block for product id to perform further actions
        except:
            res = {
                    'status':False,
                    'message':'Something went wrong'
                }
            return Response(res)

@api_view(['POST'])
def user_cart_view(request,format=None):
    token = request.data['token']
    try:
        user = user_data.objects.get(token = token)
        print(user.first_name)
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
    else :
        return Response(items)
    #quantity=1
    product_list = []
    final_sub_total = 0
    final_making_charges = 0
    shipping = 100
    tax = 1.8
    #'''for i in items:
        #prod_data = products.filter(id = i['product_id']).last()
    
    #    prod_dict = {
         #            'cart_product_id':i['id'],
         #            'id':prod_data['id'],
          #           ''''image':prod_data['image'].split(',')[0],
           #          'title':prod_data['title'],'''
            #         'quantity':i['quantity']'''
                 #   }
    return Response("in progress")