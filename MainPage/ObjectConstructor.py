# -*- coding: utf-8 -*-
import urllib
import urllib2
import re
import sys
default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)



class ObjectConstructor(object):

    def __init__(self, id, query_words):
        """通过目标url的id和查询的单词列表来初始化对象"""

        with open('info/' + str(id) +'.txt', 'r') as f:
            self.url = f.readline()[:-1]
            self.title = f.readline()[:-1]
            self.text_string = f.readline()[:-1]
            self.rank = float(f.readline()[:-1])
            year = int(f.readline()[:-1])
            month = int(f.readline()[:-1])
            day = int(f.readline()[:-1])
            self.time = (year - 2000) + month * 12 + day

        self.query_words = query_words
        self.all_words = ''.join(self.query_words)


    def get_title(self):
        # 限制只显示20个字符，如果超过了20个，那么加上省略号
        title = unicode(self.title)[:20]
        if len(title) == 20:
            title += '..'

        ans = ''
        for item in title:
            try:
                if item not in self.all_words:
                    ans += (r'<span>' + item + r'</span>')
                else:
                    ans += (r'<strong>' + item + r'</strong>')
            except:
                ans += (r'<span>' + item + r'</span>')
        return ans


    def get_text(self):
        """获取应当展示在首页的省略版本的内容"""
        origin = ''
        try:
            self.text_string = unicode(self.text_string)
            cur = self.text_string.find(self.query_words[0])
            i = cur - 40
            if i < 0:
                i = 0
            j = cur + 90
            origin = self.text_string[i:j]
        except:
            pass

        ans = ''
        for item in origin:
            try:
                if item not in self.all_words:
                    ans += item
                else:
                    ans += (r'<strong>' + item + r'</strong>')
            except:
                ans += (r'<span>' + item + r'</span>')
        return ans


    def get_url_ori(self):
        return self.url











