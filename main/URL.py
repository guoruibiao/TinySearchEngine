# -*- coding: utf-8 -*-
import sys
default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)


class URL(object):
    #每个URL对象的几个特征

    def __init__(self, url, id_):
        self.url = url
        self.id = id_
        self.text = ''
        self.links = []  # 指向的链接, id是多少, 这个是后来建立的
        self.links_id = []