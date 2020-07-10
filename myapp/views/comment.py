from myapp.models import *
from django.shortcuts import HttpResponse
from django.shortcuts import render
from django.http import JsonResponse
from django.contrib import messages
from django.core import serializers

def getCommentById(request):
    '''
    通过评论ID获取评论
    '''
    return JsonResponse()

def getCommentByMid(request):
    '''
    通过电影ID获取评论
    '''
    return JsonResponse()

def getCommentByUid(request):
   '''
    通过用户ID获取评论
    '''
    return JsonResponse()

def getCommentByUidAndMid(request):
    '''
    通过用户ID和电影ID获取评论
    '''
    return JsonResponse()

def addComment(request):
   '''
    添加评论
    '''
    return JsonResponse()
