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
# from django.views.decorators.csrf import csrf_exempt
#----------------------------restAPI--------------------------------------------------
from rest_framework.decorators import parser_classes,api_view
from rest_framework.parsers import MultiPartParser,FormParser
from rest_framework.response import Response

#----------------------------models---------------------------------------------------
from realvedic_app.models import user_data,user_address

#----------------------------extra---------------------------------------------------
import simplejson as json


@api_view(['POST'])
def userAccountView(request,format=None):
    token=request.data['token']
    user=user_data.objects.get(token=token)
    user_address_val=user_address.objects.get(user_id=user.id)
    res={}
    res['first_name']=user.first_name
    res['last_name']=user.last_name
    res['email']=user.email
    res['phone_code']=user.phone_code
    res['phone_number']=user.phone_no
    res['dob']=user.dob 
    res['address_line_1']=user_address_val.add_line_1 
    res['address_line_2']=user_address_val.add_line_2
    res['city']=user_address_val.city
    res['state']=user_address_val.state
    res['country']=user_address_val.country
    res['pincode']=user_address_val.pincode

    
    return Response(res)
@api_view(['POST'])
def UserAccountEdit(request,format=None):
    token=request.data['token']
    user=user_data.objects.get(token=token)
    #user_address_val=user_address.objects.get(user_id=user.id)'''
    
    first_name = request.data['first_name']
    last_name = request.data['last_name']
    gender = request.data['gender']
    dob = request.data['dob']
    email = request.data['email']
    phone_code = request.data['phone_code']
    phone_no = request.data['phone_no']
    
    #------------Address call
    add_line_1 = request.data['add_line_1']
    add_line_2 = request.data['add_line_2']
    landmark = request.data['landmark']
    city = request.data['city']
    state = request.data['state']
    country = request.data['country']
    pincode = request.data['pincode']


    try:
        user_data.objects.filter(token = token).update(
                                                        first_name = first_name,
                                                        last_name= last_name,
                                                        email = email,
                                                        gender = gender,
                                                        dob = dob,
                                                        phone_code = phone_code,
                                                        phone_no = phone_no,
                                                      )
        user_address.objects.filter(user_id=user.id).update(
                                                            add_line_1=add_line_1,
                                                            add_line_2=add_line_2,
                                                            landmark=landmark,
                                                            city=city,
                                                            state=state,
                                                            country=country,
                                                            pincode=pincode

                                                            
                                                                )
        res = {
               'status':True,
               'message': 'Profile updated successfully'
              }
    except:
        res = {
                'status':False,
                'message':'Something went wrong'
              }
    return Response(res)
