import jieba

class Spliter(object):
    def __init__(self, urls):
        self.urls = urls
        self.stop_word = set()
        self.allword = dict() #有哪些网页指向了这个单词

    def pre_read(self):
        with open('stopword.txt', 'r', encoding='utf-8') as f:
            for line in f:
                if line[:-1] != '':
                    self.stop_word.add(line[:-1])

    def constructor(self):
        self.pre_read()
        for URL in self.urls:
            after = jieba.cut_for_search(URL.text)
            for item in after:
                if item not in self.stop_word:
                    if item not in self.allword:
                        self.allword[item] = []
                        self.allword[item].append(URL.id)
                    else:
                        self.allword[item].append(URL.id)
        self.urls.clear()
        return self.allword

    #先仅仅按照相关新排序
    def query(self, word):
        self.constructor()
        words = jieba.cut_for_search(word)
        rawlist = []
        for item in words:
            if item in self.stop_word or item not in self.allword:
                continue
            rawlist.extend(self.allword[item])
        counter = dict()
        for item in rawlist:
            if item not in counter:
                counter[item] = 1
            else:
                counter[item] += 1
        ret = sorted(counter.items(), key=lambda d: d[1], reverse=True)
        return [x[0] for x in ret]

