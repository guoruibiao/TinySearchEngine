
class URL(object):
    #每个URL对象的几个特征

    def __init__(self, url, id_, text, links_to): #去掉空格和英文之后的内容
        self.url = url
        self.id = id_
        self.text = text
        self.links = links_to  # 指向的链接, id是多少, 这个是后来建立的
        self.links_id = []