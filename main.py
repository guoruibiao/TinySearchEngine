

from spider import *
from Constructor import *
#from rankpage import *
from URL import *
from utility import *
#from spliter import *
import time
import json





import sys

oldStdout = None
logfile = None
logfile = open('log.txt','w+')
oldStdout = sys.stdout
sys.stdout = logfile


def WriteToFile(url):
    f = open('info/' + str(url.id) + '.txt', 'w+', encoding='utf-8')
    f.write(url.url)
    f.write('\n')
    f.write(str(len(url.link_to)))
    f.write('\n')
    for item in url.link_to:
        f.write(str(item))
        f.write('\n')
    #f.write(StringFilter(GetHtmlStr(url.url)))
    if url.url in global_cache_text:
        f.write(global_cache_text[url.url])
        #print('in.it')
    else:
        f.write(GetHtmltext(GetHtmlStr(url.url), url.url))
    f.write('\n')
    f.write(str(url.rank))
    f.write('\n')
    f.close()
print('Spider_start')
start = time.clock()
spider = Spider('http://news.dlut.edu.cn/')
hash_table = spider.my_multythread()
print('Spider_over')
print('construct-_start')
contr = Contructor(hash_table)
print('construct-_id')
id = contr.construct_id()
print('construct-_urls')
urls = contr.construct_urls()
print('Construct-Over')

# A = GetMatrixA(urls, id)
# ranker = RankPage(A)
# rankB = ranker.calcu()
# for i in range(len(rankB)):
#     urls[i].rank = rankB[i]
#urls = sorted(urls, key=lambda x: x.rank, reverse=True)
urls_iter = filter(lambda url: len(url.link_to) != 0, urls)
print("sort & filter Over")
#有些id被过滤掉了，因此存在的id可能不是连续的

print('Write-begin')
cnt = 0
for item in urls_iter:
    cnt += 1
    if cnt % 100 == 0:
        print('now-write', cnt)
    WriteToFile(item)
print('Write-info-over')
end = time.clock()
print(end - start, 'second_cost')





if logfile:
    logfile.close()
if oldStdout:
    sys.stdout = oldStdout



