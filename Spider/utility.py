# coding=utf-8   #默认编码格式为utf-8

from urllib import request


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

def formuler(url):
    """将url标准化"""
    if url.startswith('http') == False:
        url = 'http://news.dlut.edu.cn/' + url
    if url.endswith('#'):
        url = url[:-1]
    if url.find('/..') != -1:
        url = url.replace('/..', '')
    return url
