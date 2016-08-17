#搜索引擎项目入门版本

#概述：

主要分为两部分，爬虫爬取将关网页，存放到本地，建立倒排索引在内存中，等待用户查询

#Part I (python 3.4+)

## spider
 - 给定一个根网址，进行BFS，根据第一个网页的链接，开n个线程，1<n<100；
 - 将网址hash到set中，有必要的话，写入到文件中
 - 返回一个URL的list
 - **问题**
   - 这里根据测试的效果来看，多线程优化的效果不是很好
   - 并且似乎是由于set不是多线程安全的，不能很好的控制，set的大小
   - 返回如果是set，总是set size changed while iteration报错，返回list，正常

## utility
  - 在BFS的过程中，需要进行URL标准化的过程和URL筛选的过程
  - 两个全局缓冲区
  - **问题**
    - 这几个函数可以优化


## parser
  - 在解析网页的过程中，直接将网页的url链接和文本放到缓冲区，防止下一次重新解析
  - 获取的网页text正文，将被去掉所有的标点符号
## constructor
  - 将网址编号成0-n-1，网址-id放到一个dict中
  - 遍历所有的网址，每个网址建立一个对象返回这个结果
    - id，url，指向的网址的id列表，rank

##根据网址的指向链接数目，进行权威性排序
  - 这里由于服务器的库安装问题，直接去掉了
  - 具体rankpage算法可以参考《数学之美》
  - 已经实现的算法仍然有，优化空间（小概率事件a取值）
  - 可以根据rankpage进行排序

##过滤404页面，没有指向任何网页

##将每个URL对象写入本地
  - id 文件名
  - 几个linkto
  - 罗列linkto的id
  - 正文
  - rank值


#Part II(python 2.7)

## ObjectConstructor
  - 构造显示在网页的上的对象，从文件中获得
  - 网址，对应的id
  - 正文（无标点符号）
  - 获得标题：这里又运行了一遍爬虫但是没有使用正则，同时将数据直接格式化成html
  - 获得正文：同理将数据格式化
  - 获得网址：标准网址
  - python2和3的爬虫使用的库不同，重新实现了一遍

##spliter
  - 辅助函数，从文件中读入数据到缓存中，如果已经存在于缓存中了，直接返回
  - Spliter
    - 读入停止词白名单
    - 构造每个中文词的出现位置
    - 查询
      - 返回词语出现次数最多的50个网页
  - **问题**
      - 白名单为什么会失效？
	 

##blog主函数：
  - **问题**
    - 总是出现utf-8不能解码的问题
    - 为了不一次又一次的读取文件，只好建立缓存，为什么缓存建立在另一个文件就OK？本文件就不行，python内存释放机制是怎么样的？
    - web_app的运行顺序是什么



# Part III 


如果有继续优化的想法，可以按照以下几个方向进行优化：

- 使用mysql数据库，不使用文件，提高访问速度
- 查询的时候综合rank（权威性和相关性）进行综合排名
- 提供按照相关性和时间和综合性查询的选项
- 返回的结果可以使用优先队列并且提供翻页的访问需求
- 提高代码的可扩展性，如果另一个平台上线
- 解决上述细节问题

# Part IV 

Reference

- [web.py中文社区](http://www.zhihu.com/question/24226159)
- [廖雪峰的官方网站](http://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000)
- [numpy](http://blog.csdn.net/hickai/article/details/23431843)、
- [jieba分词](http://www.oschina.net/p/jieba/)
- [文本处理的一些概念](http://www.tuicool.com/articles/Q32Y3q)
- [python2的头两行](http://www.crifan.com/python_head_meaning_for_usr_bin_python_coding_utf-8/)
- [入门级别的webpy](http://www.oschina.net/question/5189_4306?fromerr=VLQo08xv)
- [webpy构建博客](http://blog.csdn.net/caleng/article/details/5712850)
- [卸载mysql](http://blog.sina.com.cn/s/blog_9f760b9d010129t8.html)
- [部署webpy到服务器](http://www.liaoxuefeng.com/article/0013738925109653a9f5fe0a82c4984ba8e8174b456d0ce000)
- [webpycookbook](http://doc.outofmemory.cn/python/webpy-cookbook/)
- [Mysql基本](http://www.cnblogs.com/BeginMan/p/3249472.html)
- [webpy数据库入门](http://www.liaoxuefeng.com/article/001373891312159987278f8f31248fd9ad8aca21a3f0e6b000)
- [讲得很好的webpy模板](http://www.jianshu.com/p/7817641efe8d)
- [其他实现](http://blog.csdn.net/napoay/article/details/51477586)

