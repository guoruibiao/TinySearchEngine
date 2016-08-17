
class URL(object):
    #每个URL对象的几个特征

    def __init__(self, url, id_):
        self.url = url
        self.id = id_
        self.link_to = [] #指向的链接, id是多少
        self.rank = -1
        self.text = ''
