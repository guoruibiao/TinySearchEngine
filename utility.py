# coding=utf-8   #默认编码格式为utf-8

from urllib import request


#全局缓冲变量
global_cache_link = dict()
global_cache_text = dict()
#全局缓冲变量

def GetHtmlLinks_from_cache(url):
    return global_cache_link[url]

def GetHtmltext_from_cache(url):
    return global_cache_text[url]

def GetHtmlStr(current_url):
    htmlstr = ''
    try:
        req = request.Request(current_url)
        # req.add_header('User-Agent', 'Mozilla/6.0')
        response = request.urlopen(req)
        data = response.read()
        htmlstr = data.decode('utf-8')
    except:
        pass
    return htmlstr


def urlfilter(url):
    """url筛选器"""
    picturesflag = ['jpg', 'jpeg', 'png', 'PNG', 'JPG', 'JPEG']
    if url.find('news.dlut.edu.cn') == -1:
        return False
    return url.endswith('html') or url.endswith('htm')



def is_chinese(uchar):
    """判断一个unicode是否是汉字"""
    if uchar >= u'\u4e00' and uchar <= u'\u9fa5':
        return True
    else:
        return False

def StringFilter(s):
    ret = ''
    for item in s:
        if is_chinese(item):
            ret += item
    return ret



def formuler(url):
    """将url标准化"""
    if url.startswith('http') == False:
        url = 'http://news.dlut.edu.cn/' + url
    if url.endswith('#'):
        url = url[:-1]
    if url.find('/..') != -1:
        url = url.replace('/..', '')
    return url
