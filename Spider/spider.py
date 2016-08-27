
import queue
import threading
from my_parser import *


import logging
logging.basicConfig(level=logging.INFO)


class Spider(object):
    def __init__(self, root_url):
        self.root_url = root_url
        self.url_queue = queue.Queue()
        self.seen = set()
        self.log_counter = 0

    def one_thread(self, start_url):
        parser = HtmlParserMainText()
        self.url_queue.put(start_url)
        while not self.url_queue.empty():
            current_url = self.url_queue.get()  # 拿出队例中第一个的url
            extract_urls = parser.settle_down(current_url)
            for next_link in extract_urls:
                if next_link in self.seen:
                    continue
                self.seen.add(next_link)
                self.url_queue.put(next_link)
                # logging
                self.log_counter += 1
                if self.log_counter % 100 == 0:
                    print('Spider_INFO ' + str(self.log_counter))
                if self.log_counter >= 100:
                    return

    def start(self):
        parser = HtmlParserMainText()
        self.seen.add(self.root_url)
        extract_urls = parser.settle_down(self.root_url)
        threads = []
        for item in extract_urls:
            if item in self.seen:
                continue
            self.seen.add(item)
            self.url_queue.put(item)
            tmp = threading.Thread(target=self.one_thread, args=(item,))
            threads.append(tmp)

        for i in range(0, len(threads)):
            t = threads[i]
            t.setDaemon(True)
            t.start()
            # print('open_one_thread_ok')
        t.join()




