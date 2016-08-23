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

def get_most_k_value(k, li):
    """从列表中找出出现次数前k个的数值"""
    counter = dict()
    for item in li:
        if item not in counter:
            counter[item] = 1
        else:
            counter[item] += 1
    ret = sorted(counter.items(), key=lambda d: d[1],reverse=True)
    return [x[0] for x in ret][:k]


class Spliter(object):
    def __init__(self):

        self.stop_word = set()
        self.cache = dict()
        self.memory = dict()
        with open('stopword.txt', 'r') as f:
            for line in f:
                if line[:-1] != '':
                    self.stop_word.add(line[:-1])


    def read_files(self):
        bad, cnt = 0, 0
        for ide in range(100000):
            filename = 'info/' + str(ide) + '.txt'
            try:
                f = open(filename, 'r')
                url = f.readline()[:-1]
                url_obj = URL(url, ide)
                n = int(f.readline()[:-1])
                for i in range(n):
                    url_obj.links_id.append(int(f.readline()[:-1]))
                url_obj.text = f.readline()[:-1]

                # 读取完成之后直接构建词语列表
                after_split_text = jieba.cut_for_search(url_obj.text)
                for word in after_split_text:
                    if word in self.stop_word:
                        continue
                    if word not in self.cache:
                        self.cache[word] = []
                    else:
                        self.cache[word].append(url_obj.id)
                #构建词语表完成，放到内存中等待取用

                bad, cnt = 0, cnt + 1
                if cnt % 100 == 0:
                    print 'Read & Construct ', cnt
                f.close()
            except IOError:

                bad += 1
                if bad == 1000:
                    break
        print 'cutting info'
        for word_, lists in self.cache.items():
            tmplist = get_most_k_value(50, lists)
            self.memory[word_] = tmplist
        self.cache.clear()


    #传入的是一个句子
    def query(self, strings):
        strings = unicode(strings)
        words = jieba.cut_for_search(strings)

        raw_list = []
        for word in words:
            if word in self.memory:
                raw_list.extend(self.memory[word])
        return get_most_k_value(50, raw_list)


