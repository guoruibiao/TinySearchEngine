# -*- coding: utf-8 -*-
import urllib
import urllib2
import re
import sys
default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)





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
    def __init__(self, id, querywords):
        with open('info/' + str(id) +'.txt', 'r') as f:
            self.url = f.readline()[:-1]
            n = int(f.readline()[:-1])
            for _ in range(n):
                f.readline()
            self.text_string = f.readline()[:-1]
        self.htmlstr = GetHtmlStr(self.url)
        self.words = querywords
    def get_title(self):
        i = self.htmlstr.find('<title>')
        j = self.htmlstr.find('</title>')
        if i == -1 or j == -1:
            i = self.htmlstr.find('<TITLE>')
            j = self.htmlstr.find('</TITLE>')
        ori = self.htmlstr[i+7:j]
        ret = ori[:20]
        if len(ret) == 20:
            ret += '..'
        tmpall = ''
        for i in self.words:
            tmpall += i
        ans = ''
        for item in ret:
            try:
                if item not in tmpall:
                    ans += (r'<span>' + item + r'</span>')
                else:
                    ans += (r'<strong>' + item + r'</strong>')
            except:
                ans += (r'<span>' + item + r'</span>')
        return ans

    def get_text(self):

        ret = ''
        try:
            self.text_string = unicode(self.text_string)
            cur = self.text_string.find(self.words[0])

            i = cur - 40
            if i < 0:
                i = 0
            j = cur + 90
            ret = self.text_string[i:j]

            # if j > len(self.text_string):
            #     ret += '..'
        except:
            pass

        tmpall = ''
        for i in self.words:
            tmpall += i
        ans = ''
        for item in ret:
            try:
                if item not in tmpall:
                    ans += item
                else:
                    ans += (r'<strong>' + item + r'</strong>')
            except:
                ans += (r'<span>' + item + r'</span>')

        return ans

    def get_url_ori(self):
        return self.url











