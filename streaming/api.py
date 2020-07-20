import json
import random
from wsgiref.simple_server import make_server

import numpy as np
import pymysql

conn = pymysql.connect(host="localhost",
                       port=3306,
                       user="root",
                       password="120114",
                       database="rec_movie",
                       charset="utf8")
cursor = conn.cursor()


class api():
    def __init__(self, ip="localhost", port=8088):
        httpd = make_server(ip, port, app=self.test)
        httpd.serve_forever()

    def test(self, environ, start_response):

        def top5(environ1, start_response1):

            start_response1('200 ok', [('Context-Type', 'textml')])
            content = environ1.get('QUERY_STRING')
            parts = content.split('&')

            sql0 = "SELECT IFNULL(message,0) FROM real_time_info"
            result = cursor.execute(sql0)

            if(result != 0):
                sql1 = "select time, message from real_time_info ORDER BY RAND() limit 2"
                cursor.execute(sql1)
                ret1 = cursor.fetchall()

                movie_id = str(ret1[0][1])
                print("test:"+movie_id)

                # sql2 = "select m_id,recommend_movie_id from recommend_movie where recommend_movie.m_id= %s"
                # cursor.execute(sql2,(movie_id))
                sql2 = "select m_id,recommend_movie_id from recommend_movie where recommend_movie.m_id="+movie_id
                cursor.execute(sql2)
                ret2 = cursor.fetchall()

                movie_list = str(ret2[0][1]).split(",")

                hostlist = []
                for i in range(5):
                    hostlist.append(random.randint(5, 15))
                hostlist.sort(reverse=True)

                finres = []
                print(movie_list)

                for i in range(5):

                    sql3 = "select m_name from movie where movie.m_id=" + \
                        movie_list[i]
                    cursor.execute(sql3)
                    ret3 = cursor.fetchall()

                    dict = {"mid": movie_list[i],
                            "hot": hostlist[i], "mname": ret3[0]}
                    finres.append(dict)
                print(finres)

                return [json.dumps({"code": 200, "finalresult": finres}).encode()]

            else:

                # sql="select mid, hot ,m_name from top5,movie where top5.mid=movie.m_id order by hot desc "
                # cursor.execute(sql)
                # ret=cursor.fetchall()

                sql1 = "select m_id ,m_name from movie ORDER BY  RAND() limit 100"
                cursor.execute(sql1)
                ret = cursor.fetchall()

                hostlist = []
                for i in range(5):
                    hostlist.append(random.randint(5, 15))
                hostlist.sort(reverse=True)

                finres = []

                for i in range(5):
                    dict = {"mid": ret[i][0],
                            "hot": hostlist[i], "mname": ret[i][1]}
                    finres.append(dict)
                # for i in ret:
                    # dict={"mid":i[0],"hot":i[1],"mname":i[2]}
                    # finres.append(dict)

                return [json.dumps({"code": 200, "finalresult": finres}).encode()]

        return top5(environ, start_response)


handler = api()