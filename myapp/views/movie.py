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
import logging
import numpy as np
from bs4 import BeautifulSoup
from lxml.html import etree
import pymysql
import itertools
import logging
import logging.handlers
import time
from log import log_file

# def log_file(id):
#     now = time.time()
#     local_time = time.localtime(now)
#     filename = time.strftime('%Y-%m-%d %H-%M-%S', local_time)
#     date_format_localtime = time.strftime('%Y-%m-%d %H:%M:%S', local_time)
#     print("log:"+id)
#     with open('E:\\Desktop\\MovieRecommendationSystem\\log\\logfile\\' + filename + '.txt', mode='a', encoding='utf-8') as file:
#         file.write(date_format_localtime+","+str(id))

headers = {
    'User-Agent':
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
}


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


#日志设置
# log_file="log\log.log"
# logger = logging.getLogger("m_id")
# logger.setLevel(level=logging.INFO)

# formatter = logging.Formatter(
#     '%(asctime)s-%(levelname)s-%(message)s')

# stream_handler = logging.StreamHandler()
# stream_handler.setFormatter(formatter)

# file_handler = logging.FileHandler(filename=log_file, encoding='utf-8')
# file_handler.setFormatter(formatter)

# logger.addHandler(file_handler)
# logger.addHandler(stream_handler)


def getMovieByName(request):
    m_name = request.GET.get('m_name', '')
    m_list = Movie.objects.filter(m_name=m_name)
    if len(m_list) == 0:
        return JsonResponse({'code': 0})
    m_list = serializers.serialize("json", m_list)
    return JsonResponse({'code': 1, 'm_list': m_list})


def getMovieByType(request):
    print("############################")
    print("getMovieByType")
    type = request.GET.get('type', '')
    count = int(request.GET.get('count', ''))
    print(count)
    print(type)
    m_list = []
    for i in Movie.objects.filter(type__contains=type):
        m_list.append(i)
    cmpfun = operator.attrgetter('rate')
    m_list.sort(key=cmpfun, reverse=True)

    if len(m_list) == 0:
        messages.error(request, '电影不存在！')
        return JsonResponse({'code': 0})

    m_list = m_list[12 * (count - 1):12 * count]
    res = []
    for i in m_list:
        x = Movie_()
        x.movieId = int(i.m_id)
        x.name = i.m_name
        x.actors = i.actor
        x.cover = i.imgurl
        x.directors = i.director
        x.genres = i.type + ' ' + i.actor
        x.officialSite = 'https://v.qq.com/'
        x.regions = i.area
        x.languages = i.language
        x.mins = i.length
        x.score = i.rate
        x.votes = 1
        x.tags = i.type
        x.storyline = ''
        x.year = ''
        x.actorIds = ''
        x.directorIds = ''
        x.releaseDate = ''
        try:
            if req.urlopen(i.imgurl).status == 200:
                x.cover = i.imgurl
            else:
                x.cover = 'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1589887458475&di=38b6dbf53b6505b7a5cb3764c1857313&imgtype=0&src=http%3A%2F%2Fimg3.doubanio.com%2Fview%2Fgroup_topic%2Flarge%2Fpublic%2Fp108048762.jpg'
        except:
            x.cover = 'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1589887458475&di=38b6dbf53b6505b7a5cb3764c1857313&imgtype=0&src=http%3A%2F%2Fimg3.doubanio.com%2Fview%2Fgroup_topic%2Flarge%2Fpublic%2Fp108048762.jpg'
        res.append(x)
    # m_list = serializers.serialize("json", res)
    m_list = json.dumps(res, default=lambda obj: obj.__dict__)
    return JsonResponse({'code': 1, 'm_list': m_list})


def getMovieById(request):
    print("############################")
    print("getMovieById")
    id = request.GET.get('id', '')
    print(id)
    print(type(id))
    log_file(id)
    m_list = Movie.objects.filter(m_id=id)
    if len(m_list) == 0:
        messages.error(request, '电影不存在！')
        return JsonResponse({'code': 0})

    res = []
    for i in m_list:
        x = Movie_()
        x.movieId = int(i.m_id)
        x.name = i.m_name
        x.actors = i.actor
        x.cover = i.imgurl
        x.directors = i.director
        x.genres = i.type + ' ' + i.actor
        x.officialSite = 'https://v.qq.com/'
        x.regions = i.area
        x.languages = i.language
        x.mins = i.length
        x.score = i.rate / 10.0
        x.tags = i.type
        x.year = ''
        try:
            if req.urlopen(i.imgurl).status != 200:
                i.imgurl = 'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1589887458475&di=38b6dbf53b6505b7a5cb3764c1857313&imgtype=0&src=http%3A%2F%2Fimg3.doubanio.com%2Fview%2Fgroup_topic%2Flarge%2Fpublic%2Fp108048762.jpg'
        except:
            i.imgurl = 'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1589887458475&di=38b6dbf53b6505b7a5cb3764c1857313&imgtype=0&src=http%3A%2F%2Fimg3.doubanio.com%2Fview%2Fgroup_topic%2Flarge%2Fpublic%2Fp108048762.jpg'

        try:
            response = requests.get('https://movie.douban.com/subject/' +
                                    i.m_id + '/',
                                    headers=headers)
            response.encoding = 'utf-8'
            soup = BeautifulSoup(response.text, "html.parser")
            x.releaseDate = soup.find("span",
                                      attrs={
                                          "property": "v:initialReleaseDate"
                                      }).get_text()
            x.releaseDate = x.releaseDate.split('(')[0]
            x.storyline = soup.find("span", attrs={
                "property": "v:summary"
            }).get_text()
            x.votes = int(
                soup.find("span", attrs={
                    "property": "v:votes"
                }).get_text())
            x.cover = etree.HTML(response.text).xpath('//img/@src')[0]
        except:
            x.storyline = '亲爱的用户，很抱歉未获取到相应数据。'
            x.releaseDate = '0000-00-00'
            x.votes = 2032805
            x.cover = i.imgurl
        x.actorIds = ''
        x.directorIds = ''
        res.append(x)
    # m_list = serializers.serialize("json", res)
    m_list = json.dumps(res, default=lambda obj: obj.__dict__)

    return JsonResponse({'code': 1, 'm_list': m_list})


def searchMovie(request):
    print("############################")
    print("searchMovie")
    tag = request.GET.get('tag', '')
    count = int(request.GET.get('count', ''))
    print(tag)
    print(count)
    m_list1 = Movie.objects.filter(type__contains=tag)
    m_list2 = Movie.objects.filter(m_name__contains=tag)
    print(len(m_list2))
    m_list3 = Movie.objects.filter(director__contains=tag)
    m_list4 = Movie.objects.filter(screenwriter__contains=tag)
    m_list5 = Movie.objects.filter(actor__contains=tag)
    m_list6 = Movie.objects.filter(area__contains=tag)
    m_list7 = Movie.objects.filter(language__contains=tag)
    m_list8 = Movie.objects.filter(language__contains=tag)
    print(type(m_list1))
    m_list = []
    for i in m_list1:
        m_list.append(i)
    for i in m_list2:
        m_list.append(i)
    for i in m_list3:
        m_list.append(i)
    for i in m_list4:
        m_list.append(i)
    for i in m_list5:
        m_list.append(i)
    for i in m_list6:
        m_list.append(i)
    for i in m_list7:
        m_list.append(i)
    for i in m_list8:
        m_list.append(i)
    if len(m_list) == 0:
        messages.error(request, '电影不存在！')
        return JsonResponse({'code': 0})

    m_list = m_list[12 * (count - 1):12 * count]
    res = []
    for i in m_list:
        x = Movie_()
        x.movieId = int(i.m_id)
        x.name = i.m_name
        x.actors = i.actor
        x.cover = i.imgurl
        x.directors = i.director
        x.genres = i.type + ' ' + i.actor
        x.officialSite = 'https://v.qq.com/'
        x.regions = i.area
        x.languages = i.language
        x.mins = i.length
        x.score = i.rate
        x.votes = 1
        x.tags = i.type
        x.storyline = ''
        x.year = ''
        x.actorIds = ''
        x.directorIds = ''
        x.releaseDate = ''
        try:
            if req.urlopen(i.imgurl).status == 200:
                x.cover = i.imgurl
            else:
                x.cover = 'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1589887458475&di=38b6dbf53b6505b7a5cb3764c1857313&imgtype=0&src=http%3A%2F%2Fimg3.doubanio.com%2Fview%2Fgroup_topic%2Flarge%2Fpublic%2Fp108048762.jpg'
        except:
            x.cover = 'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1589887458475&di=38b6dbf53b6505b7a5cb3764c1857313&imgtype=0&src=http%3A%2F%2Fimg3.doubanio.com%2Fview%2Fgroup_topic%2Flarge%2Fpublic%2Fp108048762.jpg'
        res.append(x)
    # m_list = serializers.serialize("json", res)
    m_list = json.dumps(res, default=lambda obj: obj.__dict__)
    return JsonResponse({'code': 1, 'm_list': m_list})


def getMoviesByIds(mid_list):
    m_list = []
    for id in mid_list:
        temp = Movie.objects.filter(m_id=id)
        if len(temp) > 0:
            m_list.append(temp[0])
    return m_list


def getRecommendMovie(request):
    print("############################")
    print("getRecommendMovie")
    m_id = request.GET.get('id', '')
    count = int(request.GET.get('count', ''))
    type = Movie.objects.filter(m_id=m_id)[0].type.split('/')[0]
    print(type)
    print(m_id)
    print(count)
    # log_file(m_id)
    mid_list = RecommendMovie.objects.filter(m_id=m_id)[0].recommend_movie_id
    mid_list = mid_list.split(',')

    if len(mid_list) == 0:
        m_list = Movie.objects.filter(type=type)
    else:
        m_list = getMoviesByIds(mid_list)
    if len(m_list) >= 6 * count:
        m_list = m_list[6 * (count - 1):6 * count]
    elif len(m_list) >= 6 * (count - 1):
        m_list = m_list[6 * (count - 1):]
    else:
        m_list = []
    res = []
    for i in m_list:
        x = Movie_()
        x.movieId = int(i.m_id)
        x.name = i.m_name
        x.actors = i.actor
        x.cover = i.imgurl
        x.directors = i.director
        x.genres = i.type + ' ' + i.actor
        x.officialSite = 'https://v.qq.com/'
        x.regions = i.area
        x.languages = i.language
        x.mins = i.length
        x.score = i.rate
        x.votes = 1
        x.tags = i.type
        x.storyline = ''
        x.year = ''
        x.actorIds = ''
        x.directorIds = ''
        x.releaseDate = ''

        try:
            if req.urlopen(i.imgurl).status == 200:
                x.cover = i.imgurl
            else:
                x.cover = "https://pic.17qq.com/uploads/cdkmnhmkdv.jpeg"
        except:
            x.cover = "https://pic.17qq.com/uploads/cdkmnhmkdv.jpeg"
        res.append(x)
    # m_list = serializers.serialize("json", res)
    m_list = json.dumps(res, default=lambda obj: obj.__dict__)
    return JsonResponse({'code': 1, 'm_list': m_list})


def getUserRecommendMovie(request):
    print("############################")
    print("getUserRecommendMovie")
    u_id = request.GET.get('id', '')
    count = int(request.GET.get('count', ''))
    tags = request.GET.get('tags', '')
    mtypes = tags.split('/')[0]
    list1=mtypes.split(",")
    print(list1)
    print(u_id)
    print(count)
    list2=[]
    for i in range(1,len(list1)+1):
        iter = itertools.permutations(list1,i)
        list2.append(list(iter))
    mtypes_list=[]
    for item in list2:
        for i in item:
            if len(item)==1:
                mtypes_list.append("".join(i))
            else:
                mtypes_list.append("/".join(i))
    print(mtypes_list)
    m_list = []
    for item in mtypes_list:
        for i in Movie.objects.filter(type__contains=item):
            m_list.append(i)
    # 参数为排序依据的属性，可以有多个，这里是rate
    cmpfun = operator.attrgetter('star', 'rate')
    m_list.sort(key=cmpfun, reverse=True)
    print(len(m_list))
    index = 0
    res = []
    for i in m_list:
        x = Movie_()
        try:
            if req.urlopen(i.imgurl).status == 200:
                x.cover = i.imgurl
            else:
                continue
        except:
            continue

        x.movieId = int(i.m_id)
        x.name = i.m_name
        x.actors = i.actor
        x.cover = i.imgurl
        x.directors = i.director
        x.genres = i.type + ' ' + i.actor
        x.officialSite = 'https://v.qq.com/'
        x.regions = i.area
        x.languages = i.language
        x.mins = i.length
        x.score = i.rate
        x.votes = 1
        x.tags = i.type
        x.storyline = ''
        x.year = ''
        x.actorIds = ''
        x.directorIds = ''
        x.releaseDate = ''

        index += 1
        res.append(x)
        if index >= 6 * count:
            break

    if len(res) >= 6 * count:
        res = res[6 * (count - 1):6 * count]
    elif len(res) >= 6 * (count - 1):
        res = res[6 * (count - 1):]
    else:
        res = []
    m_list = json.dumps(res, default=lambda obj: obj.__dict__)
    print("finish!")
    return JsonResponse({'code': 1, 'm_list': m_list})


def getTopMovie(request):
    print("############################")
    print("getTopMovie")
    type = request.GET.get('type', '')
    count = int(request.GET.get('count', ''))
    year = request.GET.get('year', '0')
    print(count)
    print(type)
    print(year)
    m_list = []
    if year == '0':
        for i in Movie.objects.filter(type__contains=type):
            m_list.append(i)
    elif year == '-1':
        for i in Movie.objects.filter(type__contains=type):
            if int(i.star.split("-")[0]) < 1960:
                m_list.append(i)
    else:
        for y in range(int(year), (int(year) + 10)):
            for i in Movie.objects.filter(type__contains=type,
                                          star__contains=str(y)):
                m_list.append(i)
    print(len(m_list))

    cmpfun = operator.attrgetter('rate')
    m_list.sort(key=cmpfun, reverse=True)

    if len(m_list) == 0:
        messages.error(request, '电影不存在！')
        return JsonResponse({'code': 0})

    m_list = m_list[12 * (count - 1):12 * count]
    res = []
    for i in m_list:
        x = Movie_()
        x.movieId = int(i.m_id)
        x.name = i.m_name
        x.actors = i.actor
        x.cover = i.imgurl
        x.directors = i.director
        x.genres = i.type + ' ' + i.actor
        x.officialSite = 'https://v.qq.com/'
        x.regions = i.area
        x.languages = i.language
        x.mins = i.length
        x.score = i.rate / 10.0
        x.tags = i.type
        x.year = ''
        # try:
        #     if req.urlopen(i.imgurl).status != 200:
        #         try:
        #             response = requests.get('https://movie.douban.com/subject/' + i.m_id + '/', headers=headers)
        #             response.encoding = 'utf-8'
        #             x.cover = etree.HTML(response.text).xpath('//img/@src')[0]
        #         except:
        #             x.cover = i.imgurl = 'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1589887458475&di=38b6dbf53b6505b7a5cb3764c1857313&imgtype=0&src=http%3A%2F%2Fimg3.doubanio.com%2Fview%2Fgroup_topic%2Flarge%2Fpublic%2Fp108048762.jpg'
        #     else:
        #         x.cover = i.imgurl
        # except:
        #     try:
        #         response = requests.get('https://movie.douban.com/subject/' + i.m_id + '/', headers=headers)
        #         response.encoding = 'utf-8'
        #         x.cover = etree.HTML(response.text).xpath('//img/@src')[0]
        #     except:
        #         x.cover = i.imgurl = 'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1589887458475&di=38b6dbf53b6505b7a5cb3764c1857313&imgtype=0&src=http%3A%2F%2Fimg3.doubanio.com%2Fview%2Fgroup_topic%2Flarge%2Fpublic%2Fp108048762.jpg'

        try:
            if req.urlopen(i.imgurl).status != 200:
                x.cover = i.imgurl = 'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1589887458475&di=38b6dbf53b6505b7a5cb3764c1857313&imgtype=0&src=http%3A%2F%2Fimg3.doubanio.com%2Fview%2Fgroup_topic%2Flarge%2Fpublic%2Fp108048762.jpg'
            else:
                x.cover = i.imgurl
        except:
            x.cover = i.imgurl = 'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1589887458475&di=38b6dbf53b6505b7a5cb3764c1857313&imgtype=0&src=http%3A%2F%2Fimg3.doubanio.com%2Fview%2Fgroup_topic%2Flarge%2Fpublic%2Fp108048762.jpg'

        x.storyline = '亲爱的用户，很抱歉未获取到相应数据。'
        x.releaseDate = '0000-00-00'
        x.votes = 2032805
        x.actorIds = ''
        x.directorIds = ''
        res.append(x)
    # m_list = serializers.serialize("json", res)
    m_list = json.dumps(res, default=lambda obj: obj.__dict__)
    return JsonResponse({'code': 1, 'm_list': m_list})


def getRecommendUser(request):
    print("############################")
    print("getRecommendUser")
    m_id = request.GET.get('id', '')
    # 建立数据库连接
    conn = pymysql.connect(host='127.0.0.1',
                           port=3306,
                           user='root',
                           password='120114',
                           db='rec_movie',
                           charset='utf8')
    cursor = conn.cursor()
    sql1 = 'select * from movie_recommend_user where m_id = %s'
    rows = cursor.execute(sql1, (m_id))
    u_list = []
    if rows == 0:
        return JsonResponse({'code': 0, 'u_list': u_list})
    u = str(cursor.fetchone()[1]).split(',')
    for j in u:
        sql2 = 'select * from user_num where u_num = %s'
        rows = cursor.execute(sql2, (j))
        if rows:
            u_list.append({
                "id":
                cursor.fetchone()[0],
                "cover":
                'http://m.imeitou.com/uploads/allimg/2019022710/ayk4dr5gkvi.jpg'
            })
    # 关闭游标
    cursor.close()
    # 关闭连接
    conn.close()
    return JsonResponse({'code': 1, 'u_list': u_list})


def updateMovieScore(request):
    print("############################")
    print("updateMovie")
    m_id = request.GET.get('id', '')
    votes = request.GET.get('votes', '')
    score = request.GET.get('score', '')
    print("m_id:"+m_id)
    print("votes:"+votes)
    print("score:"+score)
    score=float(score)
    score=round(score,3)
    print(score)
    score=int(score*10)
    print(score)
    log_file(m_id)
    # 建立数据库连接
    conn = pymysql.connect(host='127.0.0.1',
                           port=3306,
                           user='root',
                           password='120114',
                           db='rec_movie',
                           charset='utf8')
    
    cursor = conn.cursor()
    sql1 = 'UPDATE movie SET rate= %s WHERE m_id = %s'
    # rows = cursor.execute(sql1, (score * 10, m_id))
    try:
        cursor.execute(sql1, (score , m_id))
        conn.commit()
    except:
        # 如果发生错误则回滚
        conn.rollback()
        print("更新失败")
    # 关闭游标
    cursor.close()
    # 关闭连接
    conn.close()
    return JsonResponse({'code': 1})


def exist_movie(m_id):
    m_list = Movie.objects.filter(m_id=m_id)
    if len(m_list) != 0:
        return True
    return False
