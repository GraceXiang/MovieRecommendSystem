from myapp.models import *
from django.shortcuts import HttpResponse
from django.shortcuts import render
from django.http import JsonResponse
from django.contrib import messages
from django.core import serializers
import json
from urllib import request as req
import requests
import operator
import numpy as np
from bs4 import BeautifulSoup
from lxml.html import etree
import pymysql


headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'}
class Movie_():
    movieId = ''
    name = ''
    actors = ''
    cover = ''
    directors = ''
    genres = ''
    officialSite = ''
    regions = ''
    languages = ''
    mins = ''
    score = ''
    votes = ''
    tags = ''
    storyline = ''
    year = ''
    actorIds = ''
    directorIds = ''
    releaseDate = ''

def getMovieByName(request):
   '''
    通过名字获取电影
    '''
    return JsonResponse()

def getMovieByType(request):
    '''
    通过类型获取电影
    '''
    return JsonResponse()

def getMovieById(request):
   '''
    通过ID获取电影
    '''
    return JsonResponse()


def searchMovie(request):
   '''
    搜索电影
    '''
    return JsonResponse()

def getMoviesByIds(mid_list):
   '''
    通过ID获取多个电影
    '''
    return JsonResponse()

def getRecommendMovie(request):
    '''
    获取推荐电影
    '''
    return JsonResponse()

def getUserRecommendMovie(request):
    '''
    获取用户推荐的电影
    '''
    return JsonResponse()

def getTopMovie(request):
    '''
    获取TOP5电影
    '''
    return JsonResponse()

def getRecommendUser(request):
    '''
    获取推荐用户信息
    '''
    return JsonResponse()

def updateMovieScore(request):
    '''
    更新电影分数
    '''
    return JsonResponse()

