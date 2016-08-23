


from my_parser import *
from URL import *



class Contructor_Writer(object):
    """传入一个URL的对象列表，我们需要将对象进行编号，然后将网址全部替换成编号"""
    def __init__(self, urls):
        self.id = dict()
        self.urls = urls
        # self.result = dict()
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
                print('counter ' + str(counter))
            counter += 1
            f = open('info/' + str(url.id) + '.txt', 'w+', encoding='utf-8')
            f.write(url.url), f.write('\n')
            for link in url.links:
                if link in self.id:
                    url.links_id.append(self.id[link])

            f.write(str(len(url.links_id))), f.write('\n')
            for id_ in url.links_id:
                f.write(str(id_)), f.write('\n')
            f.write(url.text), f.write('\n')
            f.write(str(0))
            f.close()









