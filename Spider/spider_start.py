
from spliter import *
from spider import *
from Constructor import *

from URL import *
from utility import *
import logging
logging.basicConfig(level=logging.INFO)
import time
import utility


# 如果原来的数据库文件存在的话，应该先删除

delete_data_base_if_exist('../Main/my_engine_data_base.db')



start = time.clock()
logging.info('Spider_Start')
spider = Spider('http://news.dlut.edu.cn/')
spider.start()
logging.info('Spider_Over')
end = time.clock()
logging.info('Spider_cost ' + str(end-start) + ' second')

start = time.clock()
logging.info('construct and write start')
ctr = Contructor_Writer(global_cache)
ctr.construct_write()
logging.info('Write over')
end = time.clock()
logging.info('Ctr cost ' + str(end-start) + ' second')

start = time.clock()
logging.info('Spliter start write to sqlite')
sp = Spliter()
sp.read_files()
end = time.clock()
logging.info('spliter cost ' + str(end-start) + ' second')


logging.info('all_done')

