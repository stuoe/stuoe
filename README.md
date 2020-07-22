<div align="center">
<img src="https://raw.githubusercontent.com/snbck/stuoe.github.io/master/static/Stuoe.png" width="300" height="300">

</div>


## Stuoe是轻量的论坛软件

* 前端使用[MDUI](https://mdui.org/)，这是一个基于 [Material Design](https://material.io/design/) 的前端框架，CSS和JS文件压缩后仅有40KB大小

* 基于[Python Flask](https://github.com/pallets/flask)，运行迅速。数据库使用[Sqlite3](https://www.sqlite.org/index.html)，不用配置数据库环境，意味着可以在任何安装Python的服务器上轻松安装并运行

* 每当回复或将帖子设为星标后，将被归纳到帖子的讨论组，如图群组。当讨论发生了新的事务，所有人都会接到[通知](https://baike.baidu.com/item/%E9%80%9A%E7%9F%A5/5957034)。讨论无阻碍

* 使用[Simditor](https://simditor.tower.im/)富文本编辑器，胜任各种排版，使用[Base64](https://www.base64decode.org/)存储图片可以减少[Requests](https://github.com/request/request)数量，减轻服务器负载，加快界面渲染速度



## 使用

#### 你需要一个安装了[Python3.8+](https://python.org/) , [nginx1.16.1](https://www.nginx.com/)的服务器

从[pypi](https://pypi.org/project/stuoe)安装（强烈不推荐）
``` bash
pip install -U stuoe
```
或者从[Github](https://github.com/)安装（实时细微版本同步）
``` bash
git clone https://github.com/stuoe/stuoe.git
cd stuoe
python setup.py install
```
新建项目
``` bash
stuoe startproject --name mysite
cd mysite
```
卸载脚手架（会冲突）
``` bash
pip uninstall stuoe
```
初始化数据库
``` bash
flask db init
flask db migrate
flask db update
```
运行在5000端口
``` bash
python app.py
```
打开[127.0.0.1:5000/install](127.0.0.1:5000/install)配置论坛信息，填写论坛名称，配置smtp邮箱，设置管理员用户等


## 生产

上面的说明只做演示，如果你想在生产中使用，请阅读该部分（预览版不推荐）


实例使用Nginx转发Flask服务，一般来讲应该用[Gunicorn](https:/gunicorn.org/)等HTTP服务器来充当Nginx与Flask服务的中间人，这里为了方便演示，就不使用HTTP服务器

#### 运行Flask服务

``` bash
cd mysite
python app.py
```

#### 配置Nginx服务
``` conf
server {    
            listen 80;
            server_name localhost;
            

            location / {
                    proxy_pass http://127.0.0.1:5000/;
            }
}
```

## 赞助
欢迎在爱发电赞助我，开发和服务器费用都是自费，任何赞助都能让我更好的开发！

在[爱发电](http://afdian.net/)赞助我  [@stuoe](http://afdian.net/@stuoe)


## 链接

* 官网:  [https://stuoe.cn](https://stuoe.cn)
* 版本 : [https://pypi.org/project/stuoe](https://pypi.org/project/stuoe)
* 论坛 : [http://discuss.stuoe.cn/](http://discuss.stuoe.cn/)

## 协议
使用[Apache License](http://www.apache.org/licenses/)，请关注[License](https://github.com/stuoe/stuoe/blob/master/LICENSE)


