
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
flask run --host 127.0.0.1 --port 5000
```
打开[127.0.0.1:5000/install](127.0.0.1:5000/install)配置论坛信息，填写论坛名称，配置smtp邮箱，设置管理员用户等


## 生产

上面的说明只做演示，如果你想在生产中使用，请阅读该部分（预览版不推荐）


实例使用Nginx转发Flask服务，一般来讲应该用[Gunicorn](https:/gunicorn.org/)等HTTP服务器来充当Nginx与Flask服务的中间人，这里为了方便演示，就不使用HTTP服务器

#### 运行Flask服务

``` bash
cd mysite
flask run --host 127.0.0.1 --port 5000
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