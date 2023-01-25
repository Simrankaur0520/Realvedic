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
from realvedic_app.models import Product_data,categoryy,images_and_banners,blogs
#from apiApp.models import user_whishlist,user_data
#from apiApp.models import metal_price,diamond_pricing


#----------------------------extra---------------------------------------------------
import simplejson as json


#Putting data into database
@api_view(['GET'])
def write_data(request,format=None):
    best_offers={
    "soup": {
      "title": "Rasam & Soups",
      "image": "",
      "offer": "Get upto 10% OFF on",
      "item": "Newly launched Soups"
    },
    "beverages": {
      "image": "",
      "offer": "20% off on",
      "item": "Beverages"
    },
    "flour": {
      "image": "",
      "offer": "20% off on",
      "item": "Spice Blend"
    },
    "spices": {
      "image": "",
      "offer": "20% off on",
      "item": "Flour Packs"
    },
    "dosa_mix": {
      "image": "",
      "offer": "20% off on",
      "item": "Dosa Mix"
    }
    }
    #-----------------Fetching data from database tables------------------------------------
    obj=Product_data.objects.filter(Status = "Active").values()
    prod_obj=Product_data.objects.values()
    category_obj=categoryy.objects.values()
    i_and_b_obj=images_and_banners.objects.values()
    blog_obj=blogs.objects.values()
    #---------------------------------------------------------------------------------------

    #------------------------list creation and initiation-----------------------------------
    res={}
    tab=[]
    dual_banner_l=[]
    top_seller_products_list=[]
    small_carousal_images_list=[]
    #single_product_details=[]
    single_product_detailss={}
    #=--------------------------------------------------------------------------------------
    #---------------------------Passing values to tab---------------------------------------
    for i in category_obj:
        tab_dict={
            'title':i['category'],
            'image':i['category_image'], 
            'color':i['category_colour']      
            }
        tab.append(tab_dict)
    #-----------------------------------passing values for banner--------------------------- 
    banner_obj=i_and_b_obj.exclude(title ="Make Best Dosa with us!")
    for i in banner_obj:
        dual_banner={
            'title':i['title'],
            'image':i['image']
            
        }
        dual_banner_l.append(dual_banner)
       
    
    #----------------------passing values for Top selling products--------------------------- 
    for i in obj:
        top_seller_products={
            'image':i["image"],
            "title":i["Product_name"],
            "weight":i["Sizes"].split("|")[0],
            "price":i["prices"].split("|")[0]
        }
    
        top_seller_products_list.append(top_seller_products)
    food=top_seller_products
   

    for i in prod_obj:
        small_carousal_images={
            "image": i["image"],
            "product_id": i["id"]
        }
        small_carousal_images_list.append(small_carousal_images)
   
   
    #------------------------------------------------------
    vdo_obj=i_and_b_obj.filter(title="Make Best Dosa with us!")
    for i in vdo_obj:

        video_data={
            'video':i['image'],
            'title':i['title']
        }
    
    single_product_detailss['video_data']=video_data
    single_product_detailss['food']=food

    
  
    blog_1=blog_obj.filter(id=1).values()
    for i in blog_1:
        blog={
            'id':i["id"],
            'image':i["image"],
            'title':i["title"],
            'Content':i["content"],
            'points':i["Points"]
        }
    
    
    #    return Response(obj)
    single_product_detailss['blog']=blog

  
   
    #-------------------------------------response assignment-----------------
    res['tab']=tab
    res['dual_banners']=dual_banner_l
    res['top_seller_products']=top_seller_products_list
    res['small_carousal_images']=small_carousal_images_list
    res['large_carousal_images']=top_seller_products_list
    res["single_product_details"]=single_product_detailss
    res['best_offers']=best_offers
    res['blog']=blog_obj

    return Response(res)


@api_view(['GET'])
def single_product_view(request,format=None):
    obj=Product_data.objects.filter(id=10).values()
    #-------------------Dictionaries and list initialisation 
    #--------------Mock description-------------------------
    desc=str("A ready dosa mix without going through the hassle of soaking, grinding, and preparing the batter. Just add water and salt, rest for few minutes, and start making tasty and healthy dosas. We have combined 80 sprouted green gram with nutritious moringa leaves and spices for a power-packed quick meal any time of the day.")
    res={}
   
    benefits={}
    pack_sizes=[]
    #-----------------assigning product_details to the response
    for i in obj:
        weight=i["Sizes"].split("|")
        prices=i["prices"].split("|")
        for j in range(len(weight)):
            weight_price={
                'weight':weight[j],
                'price':prices[j],
                'Offer_price':int(prices[j])+5
            }
            pack_sizes.append(weight_price)
        prod_details={
            'id':i["id"],
            "title":i["Product_name"],
            'description':desc,
            "original_price":i["prices"].split("|")[0],
            "offer_price":int(i["prices"].split("|")[0])+5,
            'single_image':i["image"],
            'images':["",""],
            'pack_sizes':pack_sizes}
            
        benefits={
                'title':"benefits",
                'description':i["benefits"]
            }
        ingredients={
                'title':"ingredients",
                'description':i["ingredients"]
            }
        how_to_use={
                'title':"how_to_use",
                'description':i["how_to_use"]
            }
        how_we_make_it={
                'title':"how_we_make_it",
                'description':i["how_we_make_it"]
            }
        nutrition={
                "title": "Nutritional Info per 100g (Approx)*",
                "values":
                [
                {
                    "title": "Total Fat",
                    "value": i['nutrition'].split("|")[0]
                },
                {
                    "title": "Protien",
                    "value": i['nutrition'].split("|")[1]
                },
                {
                    "title": "Carbohydrate   ",
                    "value": i['nutrition'].split("|")[2]
                },
                {
                    "title": "Energy",
                    "value": i['nutrition'].split("|")[3]
                }
                ]
                }
        
                    
    #-----------response Assignment-------------------------
        res['product_details']=prod_details
        res['benefits']=benefits
        res['ingredients']=ingredients
        res['how_to_use']=how_to_use
        res['how_we_make_it']=how_we_make_it 
        res['nutrition']=nutrition

            



        
    return Response(res)
    


       
@api_view(['GET'])
def data_input_pandas(request,format=None):
    category_obj=categoryy.objects.all()
   
    #reading and writing product data from csv file 
    '''df=pd.read_csv('product_view.csv')
    df =df.fillna(0)
    res=df.to_dict(orient='records')
    #dff=df.apply(lambda x: x.split(","),axis=0)'''
    '''for i in range(len(res)):

        Product_name =res[i]["name"]
        category =res[i]["category"]
        prices =res[i]["price"]
        Sizes =res[i]["sizes"]
        benefits =res[i]["benefits"]
        ingredients=res[i]["ingredients"]
        how_to_use=res[i]["how_to_use"]
        how_we_make_it =res[i]["how_we_make_it"]
        nutrition=res[i]["nutrition_info"]
        Status = "Inactive"
        sibling_product=res[i]["sibling_product"]
        HSN=res[i]["HSN "]
        SKU=res[i]["SKU"]
        print(category)
     

        data=Product_data(
            Product_name =Product_name,
            category =category,
            prices =prices,
            Sizes = Sizes,
            benefits =benefits,
            ingredients= ingredients,
            how_to_use=how_to_use,
            how_we_make_it =how_we_make_it,
            nutrition=nutrition,
            Status = Status,
            sibling_product=sibling_product,
            HSN=HSN,
            SKU=SKU       
            )
        data.save()'''
        #reading and writing data into databae for category details from csv file
        # 
        #   '''title="banner"+str(i)
    '''image="banner_image"+str(i)
        print(title,image)
        data=images_and_banners(
            title=title,
            image=image
        )
        data.save()'''
    ''' titlee="Make Best Dosa with us!"
            imagee="https://youtu.be/EkJC0GgY5wk"
            data=images_and_banners(
            title=titlee,
            image=imagee
            ''' 
    '''df=pd.read_csv('realvedic_category.csv')
    df =df.fillna(0)
    res=df.to_dict(orient='records')
    for i in range(len(res)):
            category= res[i]['category']
            category_colour= res[i]['category_colour']
            category_image=res[i]['image']

            data=categoryy(
                category= category,
                category_colour= category_colour,
                category_image=category_image
            )

        
            data.save()
    #return Response('success')
    category_obj=categoryy.objects.values()
    return Response(category_obj)'''
    

    
       
'''res={}
        tab=[]
        prod_tab={
            "title": obj.category,
            #"image": obj.image,
            "color": obj.category_colour,
        }
        tab.append(prod_tab)
        res['tab']:tab
    
        res="Something went wrong, Try again"
        return Response(res)


'''
