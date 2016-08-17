

from spider import *
from Constructor import *
from rankpage import *
from URL import *
from utility import *
from spliter import *
import time
import json

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

start = time.clock()
spider = Spider('http://news.dlut.edu.cn/')
hash_table = spider.my_multythread()
print('Spider_over')

contr = Contructor(hash_table)
id = contr.construct_id()
urls = contr.construct_urls()
print('Construct-Over')

A = GetMatrixA(urls, id)
ranker = RankPage(A)
rankB = ranker.calcu()
for i in range(len(rankB)):
    urls[i].rank = rankB[i]
#urls = sorted(urls, key=lambda x: x.rank, reverse=True)
urls_iter = filter(lambda url: len(url.link_to) != 0, urls)
print("Rank & sort & filter Over")
#有些id被过滤掉了，因此存在的id可能不是连续的

for item in urls_iter:
    WriteToFile(item)
print('Write-info-over')
end = time.clock()
print(end - start, 'second_cost')














