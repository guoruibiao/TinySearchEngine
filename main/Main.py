# -*- coding: utf-8 -*-
import sys
import jieba
default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)

import web
from spliter import *
from URL import *
from ObjectConstructor import *




urls = ('/Binoocle', 'Index',)

app = web.application(urls, globals())
render = web.template.render('templates')
sp = Spliter()



#首页类
class Index:
    def GET(self):
        return render.index()
    def POST(self):
        contents = web.input()
        print contents
        targets = list(jieba.cut_for_search(contents['title']))
        idlist = sp.query(contents['title'])
        print contents['title']
        shows = []
        for item in idlist:
            shows.append(ObjectConstrcutor(item, targets))
        return render.main(shows)

if __name__ == '__main__':
    sp.read_files()
    print 'read_over'
    app.run()







