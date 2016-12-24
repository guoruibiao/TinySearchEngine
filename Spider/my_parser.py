#!/usr/bin.env python
# 获取正文内容获取链接获取图片

from html.parser import HTMLParser
from re import sub
from utility import *
from URL import *
global_cache = []
global_url_counter = 0

import logging
logging.basicConfig(level=logging.INFO)

class HtmlParserMainText(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.text = []
        self.link = []

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
            self.text.append(data.strip())

    def get_html_str(self, current_url):
        html_str = ''
        try:
            req = request.Request(current_url)
            # req.add_header('User-Agent', 'Mozilla/6.0')
            response = request.urlopen(req)
            data = response.read()
            html_str = data.decode('utf-8')
        except:
            pass
        return html_str

    def settle_down(self, url):

        global global_url_counter
        self.text = []
        self.link = []
        html_str = self.get_html_str(url)

        def get_title(html_str):

            i = html_str.find('<title>')
            j = html_str.find('</title>')
            if i == -1 or j == -1:
                i = html_str.find('<TITLE>')
                j = html_str.find('</TITLE>')
            return html_str[i + 7:j]
        origin_title = get_title(html_str)

        def get_time(html_str):
            import re
            grouppattern = re.compile(r'(\d+)-(\d+)-(\d+)')
            biggest = 0
            record = (0, 0, 0)
            target = grouppattern.findall(html_str)
            if not target:
                return record
            for year, month, day in target:
                tmp = (int(year)-2000) * 365 + 12 * int(month) + int(day)
                if tmp > biggest:
                    biggest, record = tmp, (year, month, day)
            return record
        time = get_time(html_str)


        response_string = sub('<script[^>]*?>[^>]*?</script>', '', html_str)  # Delete all scripts
        self.feed(response_string)
        self.close()

        chinese_text = ''
        for string in self.text:
            for char in string:
                if is_chinese(char):
                    chinese_text += char

        links_to = []
        for link in self.link:
            link = formuler(link)
            if urlfilter(link):
                links_to.append(link)

        global_cache.append(URL(url, global_url_counter, origin_title, chinese_text, links_to, time))
        global_url_counter += 1
        return links_to














