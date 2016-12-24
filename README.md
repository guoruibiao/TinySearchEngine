
# Part I


- [**首页-搜索引擎**](115.159.97.236:8080/Binoocle)
- [**范围-大工新闻网**](http://news.dlut.edu.cn/)


# Part II

### Spider爬虫程序

- 以根节点，进行```BFS```，多线程，同时调用```parser```进行网页解析，放到全局缓冲区。
- 将缓冲区中的```URL```对象进一步处理，网址用索引替换，```Rankpage```算法，计算权威性排名，将属性写入到文件。
- 读取文件，以```unicode```建立倒排索引，放到数据库中。

### webpy主程序

- 建立首页，查询页的模板。
- 封装数据库查询操作。
- 查询数据库，返回```list[int]```，含有查询文字的网页索引。
- 根据索引，读取文件信息，根据权威性或时间（默认是根据时间），建立前```100```个渲染对象。

# Part III

### TODO

- 学习下前端的知识，提供翻页和排序选项的接口。
- 提高响应速度。


# Part IV

### Reference

- [web.py中文社区](https://www.oschina.net/question/tag/webpy)
- [廖雪峰的官方网站](http://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000)
- [Numpy](http://blog.csdn.net/hickai/article/details/23431843)
- [jieba分词](http://www.oschina.net/p/jieba/)
- [文本处理的概念](http://www.tuicool.com/articles/Q32Y3q)
- [python2_headers](http://www.crifan.com/python_head_meaning_for_usr_bin_python_coding_utf-8/)
- [入门级别的webpy](http://www.oschina.net/question/5189_4306?fromerr=VLQo08xv)
- [webpy构建博客](http://blog.csdn.net/caleng/article/details/5712850)
- [部署webpy到服务器](http://www.liaoxuefeng.com/article/0013738925109653a9f5fe0a82c4984ba8e8174b456d0ce000)
- [webpycookbook](http://doc.outofmemory.cn/python/webpy-cookbook/)
- [Mysql基本](http://www.cnblogs.com/BeginMan/p/3249472.html)
- [webpy数据库入门](http://www.liaoxuefeng.com/article/001373891312159987278f8f31248fd9ad8aca21a3f0e6b000)
- [webpy模板](http://www.jianshu.com/p/7817641efe8d)
- [其他实现](http://blog.csdn.net/napoay/article/details/51477586)
- [Sqlite](http://www.yiibai.com/sqlite/sqlite_python.html)
- [Sqlite](http://www.cnblogs.com/zibuyu/p/3564408.html)






