


from my_parser import *
from URL import *
from rankpage import *
import logging
logging.basicConfig(level=logging.INFO)

class Contructor_Writer(object):
    """传入一个URL的对象列表，将对象进行编号，然后将网址全部替换成编号,计算每个编号的rank，信息写入文件"""
    def __init__(self, urls):
        self.id = dict()
        self.urls = urls

    def get_id(self):

        for url_obj in self.urls:
            self.id[url_obj.url] = url_obj.id
        return self.id

    def construct_write(self):
        if len(self.id) == 0:
            self.get_id()

        counter = 0
        for url in self.urls:
            if counter % 100 == 0:
                logging.info('counter_INFO ' + str(counter))
            counter += 1
            for link in url.links:
                if link in self.id:
                    url.links_id.append(self.id[link])


        A = GetMatrixA(self.urls)
        caculator = RankPageAlgorithm(A)
        ranker = caculator.calcu()


        logging.debug('now_len_url_DBG', len(self.urls))

        for url in self.urls:
            f = open('info/' + str(url.id) + '.txt', 'w+', encoding='utf-8')
            f.write(url.url), f.write('\n')
            f.write(url.text), f.write('\n')
            try:
                f.write(str(ranker[url.id]))
            except:
                logging.debug('over-flow', url.id)

            f.close()









