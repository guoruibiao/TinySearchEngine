


from my_parser import *
from URL import *
class Contructor(object):

    def __init__(self, seen):
        self.seen = seen
        self.id = dict()
        self.urls = []

    def construct_id(self):
        cnt = 0
        for item in self.seen:
            self.id[item] = cnt
            cnt += 1
        return self.id

    def construct_urls(self):
        for url in self.seen:
            this_x = self.id[url]
            temp_obj = URL(url, this_x)
            html_str = GetHtmlStr(url)
            if url in global_cache_link:
                links = GetHtmlLinks_from_cache(url)
            else:
                links = GetHtmlLinks(html_str, url)
            for item in links:
                #BUGFIX
                # set: size changed or list: key error
                if item in self.id:
                    tar_x = self.id[item]
                    temp_obj.link_to.append(tar_x)
            self.urls.append(temp_obj)

        return self.urls



