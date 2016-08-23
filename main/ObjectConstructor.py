# -*- coding: utf-8 -*-
import urllib
import urllib2
import re
import sys
default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)



"""python2 和 3的写法有点区别"""
def GetHtmlStr(current_url):
    htmlstr = ''
    try:
        req = urllib2.Request(current_url)
        # req.add_header('User-Agent', 'Mozilla/6.0')
        response = urllib2.urlopen(req)
        data = response.read()
        htmlstr = data.decode('utf-8')
    except:
        pass
    return htmlstr


class ObjectConstrcutor(object):

    def __init__(self, id, query_words):
        """通过目标url的id和查询的单词列表来初始化对象"""
        with open('info/' + str(id) +'.txt', 'r') as f:
            self.url = f.readline()[:-1]
            n = int(f.readline()[:-1])
            for _ in range(n):
                f.readline()
            self.text_string = f.readline()[:-1]
        self.html_str = GetHtmlStr(self.url)
        self.query_words = query_words

    def get_title(self):
        i = self.html_str.find('<title>')
        j = self.html_str.find('</title>')
        if i == -1 or j == -1:
            i = self.html_str.find('<TITLE>')
            j = self.html_str.find('</TITLE>')

        origin = self.html_str[i+7:j]
        title = origin[:20]
        if len(title) == 20:
            title += '..'

        # 通过列表建立起来了一个句子
        all_word = ''
        for word in self.query_words:
            all_word += word
        ans = ''
        for item in title:
            try:
                if item not in all_word:
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

        # 通过列表建立起来了一个句子
        all_word = ''
        for word in self.query_words:
            all_word += word

        ans = ''
        for item in origin:
            try:
                if item not in all_word:
                    ans += item
                else:
                    ans += (r'<strong>' + item + r'</strong>')
            except:
                ans += (r'<span>' + item + r'</span>')
        return ans

    def get_url_ori(self):
        return self.url











