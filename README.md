#python blog
一个用python3.5实现的个人博客网站，内含简单的ORM框架和Web框架。

此博客基本按照[廖雪峰的python3教程](http://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001432170876125c96f6cc10717484baea0c6da9bee2be4000)实战部分与[灰手的修改](https://github.com/moling3650/mblog)。

###ORM框架
简化
先将数据库连接池与select\delete\update等SQL语句的封装，将select封装为select函数，由于delete\update无返回列表封装为execute。ORM实现model层与持久化层的模块化通信。只需将与数据库中表对应的模型类进行描述即可，模型类需继承Model类，Model类通过集成dict并通过metaclass(ModelMetaclass)进行映射便可实现模型到SQL的转变。ModelMetaclass通过__new__方法在创建对象时实现数据库主键、其他属性的分类并生成基本SQL语句。而Model类通过整理好的主键、SQL语句等实现基本的查询与存储。

###Web框架
通过调用add_routes实现路由封装，将URL与HTTP方法传到请求处理函数进行处理，在调用请求处理函数前调用RequestHandler的__call__方法，完成请求参数与request的封装，将参数传入到请求处理函数进行处理，其中请求处理函数使用装饰器进行GET\POST封装。请求函数处理后将结果传入middlerwared的response_factory进行返回的response统一封装。

###环境
可通过pip install -r requirements.txt命令安装。

###项目结构

    mblog/                    <--根目录
    |
    +-conf/                   <--服务器配置目录
    |
    +-db_init/                <--数据库初始化文件目录
    |
    +-log/                    <--服务器日志目录
    |
    +-www/                    <--web项目目录
    	|
		+-config/             <--项目配置目录
		|
		+-app/                <--app目录
		|	|
		|	+-frame/          <--web和orm框架
		|	|
		|	+-static/          <--静态文件
		|	|
		|	+-templates/       <--模板文件
		|	|
		|	+__init__.py       <--app初始化
		|	|
		|	+factorys.py       <--工厂函数
		|	|
		|	+models.py         <--模型（数据库的表）
		|	|
		|	+-route.py         <--路由
		|   |
		|   +-api.py       　　<-- api接口
		|
		orm_test.py           <--测试orm
		|
		pymonitor.py          <--监视器
		|
		run.py                <--主运行文件
		
