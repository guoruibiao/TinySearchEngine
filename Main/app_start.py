# -*- coding: utf-8 -*-
import sys
import jieba

default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)


import web
from Queryer import *
from ObjectConstructor import *
import time

urls = ('/Binoocle', 'Index', '/Like', 'Like', )

app = web.application(urls, globals())
render = web.template.render('templates')


# 首页类
class Index:
    def GET(self):
        timer = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))
        visiter = web.ctx['ip']
        f = open('log.txt', 'a+')
        f.write('Index ' + timer + ' ' + visiter + '\n')
        f.close()
        return render.index()

    def POST(self):
        contents = web.input()
        timer = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))
        visiter = web.ctx['ip']
        f = open('log.txt', 'a+')
        f.write('Post ' + timer + ' ' + visiter + ' ' + contents['title'] + '\n')
        f.close()
        
        targets = list(jieba.cut_for_search(contents['title']))# 关键词列表
        sq = SQL_queryer('my_engine_data_base.db')
        idlist = sq.query(contents['title']) # 和关键词相关性比较强的那些网址的id

        print contents['title']
        shows = []

        for id in idlist:
            try:
                shows.append(ObjectConstructor(id, targets))
            except:
                pass
                # print 'can not construct obj ', id
                # obj的构造函数可能出现异常，在这里统一舍弃这个对象
        shows = sorted(shows, key=lambda x: x.time, reverse=True)
        return render.main(shows)

class Like:
    def GET(self):
        timer = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))
        visiter = web.ctx['ip']
        f = open('log.txt', 'a+')
        f.write('Like ' + timer + ' ' + visiter + '\n')
        f.close()

        return render.like()

if __name__ == '__main__':
    print 'Ready...'
    app.run()

