
# Part I

### Sketch

- [Click Here](http://zhanglanqing.cn:8080/Binoocle)
- The URL : 115.159.97.236:8080/Binoocle
- Domain : http://zhanglanqing.cn:8080/Binoocle

### Website

- http://news.dlut.edu.cn/


# Part II 

### More optimizations to do.

- 查询的时候综合rank算法（权威性和相关性）进行综合排名
- 提供查询的选项,翻页的选项
- 提高代码的可扩展性，兼容性


# Part III

### Reference

- [web.py中文社区](http://www.zhihu.com/question/24226159)
- [廖雪峰的官方网站](http://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000)
- [numpy](http://blog.csdn.net/hickai/article/details/23431843)
- [jieba分词](http://www.oschina.net/p/jieba/)
- [文本处理的概念](http://www.tuicool.com/articles/Q32Y3q)
- [python2的头两行](http://www.crifan.com/python_head_meaning_for_usr_bin_python_coding_utf-8/)
- [入门级别的webpy](http://www.oschina.net/question/5189_4306?fromerr=VLQo08xv)
- [webpy构建博客](http://blog.csdn.net/caleng/article/details/5712850)
- [卸载mysql](http://blog.sina.com.cn/s/blog_9f760b9d010129t8.html)
- [部署webpy到服务器](http://www.liaoxuefeng.com/article/0013738925109653a9f5fe0a82c4984ba8e8174b456d0ce000)
- [webpycookbook](http://doc.outofmemory.cn/python/webpy-cookbook/)
- [Mysql基本](http://www.cnblogs.com/BeginMan/p/3249472.html)
- [webpy数据库入门](http://www.liaoxuefeng.com/article/001373891312159987278f8f31248fd9ad8aca21a3f0e6b000)
- [webpy模板](http://www.jianshu.com/p/7817641efe8d)
- [其他实现](http://blog.csdn.net/napoay/article/details/51477586)
- [sqlite](http://www.yiibai.com/sqlite/sqlite_python.html)
- [sqlite](http://www.cnblogs.com/zibuyu/p/3564408.html)


# Part IV



### Spider爬虫程序

- 以根节点，进行BFS，多线程，同时调用parser进行网页解析，建立对象，放到全局缓冲区。
- 将缓冲区中的对象进一步处理，网址用索引替换，计算一个网页能够链接到哪些网页等额外的信息，进一步处理成另外一种对象。
- 将对象信息以文件的形式，```id.txt```存放到磁盘。
- 读取文件，以```unicode```建立倒排索引，放到数据库中。

### webpy主程序

- 建立首页，查询页的模板。
- 封装数据库查询操作。建立webpy框架。
- 查询数据库，返回，含有```list[int]```，含有查询文字的网页索引。
- 根据索引，读取文件信息，建立渲染对象。

