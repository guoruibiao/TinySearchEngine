

from spider import *
from Constructor import *
#from rankpage import *
from URL import *
from utility import *
#from spliter import *
import time


start = time.clock()
print('Spider_start')
spider = Spider('http://news.dlut.edu.cn/')
spider.start()
print('Spider Over')
end = time.clock()
print('Spider cost ', end-start, ' second')

start = time.clock()
print('construct and write start')
ctr = Contructor_Writer(global_cache)
ctr.construct_write()
print('Write over')
end = time.clock()
print('Ctr cost ', end-start, ' second')






