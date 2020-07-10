from myapp.models import *
from django.shortcuts import HttpResponse
from django.shortcuts import render
from django.http import JsonResponse
from django.contrib import messages
from django.core import serializers

def getRatingById(request):
    '''
    通过ID获取排名
    '''
    return JsonResponse()

def getRatingByMid(request):
   '''
    通过电影ID获取排名
    '''
    return JsonResponse()

def getRatingByUid(request):
    '''
    通过用户ID获取排名
    '''
    return JsonResponse()

def getRatingByUidAndMid(request):
    '''
    通过用户ID和电影ID获取排名
    '''
    return JsonResponse()

def addRating(request):
    '''
    添加排名
    '''
    return JsonResponse()
