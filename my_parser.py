#!/usr/bin.env python
# 获取正文内容获取链接获取图片

from html.parser import HTMLParser
from re import sub
from utility import *

class HtmlParserMainText(HTMLParser):

    def __init__(self, url):
        HTMLParser.__init__(self)
        self.text = []
        self.link = []
        self.url = url
    def handle_starttag(self, tag, attrs):
        if tag == "p":
            self.text.append("\n")
        elif tag == 'a':
            for name, value in attrs:  # 实际上是一个元组的列表
                if name == 'href':
                    self.link.append(value)
        else:
            pass

    def handle_data(self, data):
        if len(data.strip()) > 0:
            # print(data)
            self.text.append(data.strip())

    def save_link(self, ret):
        global_cache_link[self.url] = ret

    def save_text(self, ret):
        global_cache_text[self.url] = ret



def GetHtmlLinks(htmlstr, url):
    response_string = sub('<script[^>]*?>[^>]*?</script>', '', htmlstr)  # delete all scripts
    parser = HtmlParserMainText(url)
    parser.feed(response_string)

    ret = []
    for item in parser.link:
        item = formuler(item)
        if urlfilter(item):
            ret.append(item)
    parser.save_link(ret)
    parser.close()
    return ret



def GetHtmltext(htmlstr, url):
    response_string = sub('<script[^>]*?>[^>]*?</script>', '', htmlstr)  # delete all scripts
    parser = HtmlParserMainText(url)
    parser.feed(response_string)

    ret = ''
    for string in parser.text:
        for item in string:
            if is_chinese(item):
                ret += item
    parser.save_text(ret)
    parser.close()
    return ret




