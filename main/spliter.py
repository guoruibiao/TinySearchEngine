# -*- coding: utf-8 -*-
import urllib
import urllib2
import re
import sys
from URL import *
default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)

import jieba



global_cache_word = dict()
global_cache_files = []

def Readfiles():
    global global_cache_files
    if global_cache_files:
        return global_cache_files

    bad = 0
    cnt = 0
    for ide in range(100000):
        filename = 'info/' + str(ide) + '.txt'
        try:
            f = open(filename, 'r')
            url = f.readline()[:-1]
            tmp = URL(url, ide)
            n = int(f.readline()[:-1])
            for i in range(n):
                tmp.link_to.append(int(f.readline()[:-1]))
            tmp.text = f.readline()[:-1]
            tmp.rank = float(f.readline()[:-1])
            global_cache_files.append(tmp)
            bad = 0
            cnt += 1
            if cnt % 100 == 0:
                print 'read', cnt
        except:
            bad += 1
            if bad == 100:
                break

    return global_cache_files


class Spliter(object):
    def __init__(self, urls):
        self.urls = urls
        self.stop_word = set()


    def pre_read(self):
        with open('stopword.txt', 'r') as f:
            for line in f:
                if line[:-1] != '':
                    self.stop_word.add(line[:-1])

    def constructor(self):
        if global_cache_word:
            return
        self.pre_read()
        cnt = 0
        for URL in self.urls:
            cnt += 1
            if cnt % 100 == 0:
                print 'construct-', cnt
            after = jieba.cut_for_search(URL.text)
            for item in after:
                if item not in self.stop_word:
                    if item not in global_cache_word:
                        global_cache_word[item] = []
                        global_cache_word[item].append(URL.id)
                    else:
                        global_cache_word[item].append(URL.id)

    #先仅仅按照相关新排序
    def query(self, word):
        word = unicode(word)
        words = jieba.cut_for_search(word)
        rawlist = []
        # BUG-TO-FIX-白名单不起作用了
        for item in words:
            if item in self.stop_word:
                #print 'stop_word'
                continue
            if item not in global_cache_word:
                #print 'not in'
                continue
            rawlist.extend(global_cache_word[item])
        counter = dict()
        for item in rawlist:
            if item not in counter:
                counter[item] = 1
            else:
                counter[item] += 1
        ret = sorted(counter.items(), key=lambda d: d[1], reverse=True)
        return [x[0] for x in ret][:50]

