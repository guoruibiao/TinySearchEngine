
import queue
import threading
from my_parser import *

class Spider(object):
    
    def __init__(self, rooturl):
        self.root_url = rooturl
        self.counter = 0
        self.url_queue = queue.Queue()
        self.seen = set()
        self.f = open("rec.txt", "w")
        self.maxlen = 20000
    def one_thread(self, start_url):
        
        self.url_queue.put(start_url)
        while not self.url_queue.empty() and self.counter < self.maxlen:
            current_url = self.url_queue.get()  # 拿出队例中第一个的url
            html_str = GetHtmlStr(current_url)
            if html_str != '':
                extract_urls = GetHtmlLinks(html_str, current_url)
                for item in extract_urls:
                    if item == '' or item in self.seen:
                        continue
                    self.seen.add(item)
                    self.counter += 1
                    ##LOG##
                    if self.counter % 1000 == 0:
                        print(self.counter)
                    self.f.write(str(item))
                    self.f.write('\n')
                    ##LOG##
                    self.url_queue.put(item)


    def my_multythread(self):

        self.seen.add(self.root_url)
        html_str = GetHtmlStr(self.root_url)
        extract_urls = GetHtmlLinks(html_str, self.root_url)
        threads = []
        for item in extract_urls:
            if item == '' or item in self.seen:
                continue
            self.seen.add(item)
            self.f.write(str(item))
            self.f.write('\n')
            self.url_queue.put(item)
            tmp = threading.Thread(target=self.one_thread, args=(item,))
            threads.append(tmp)

        for i in range(0, len(threads)):
            t = threads[i]
            t.setDaemon(True)
            t.start()
            #print('dbg-open-thread')
        t.join()
        return list(self.seen)
        #return self.seen