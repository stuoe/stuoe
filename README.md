# Stuoe Framework!
## 改用Stuoe！
##### 简单部署：stuoe论坛框架基于Python flask和vuejs。它只能通过安装Python3.8和一些依赖关系库来轻松运行。使用SQLite3时不需要复杂的数据库配置
##### 使用Vuejs构建页面时，平均资源大约为1M..Stuoe不会在请求时渲染。相反，它在加载后调用API来获取数据。首先让用户看到界面，然后加载内容
##### Stuoe很漂亮。支持主题颜色切换、人性化通知提示框、隐藏菜单。没有美丽的设计就没有地方
## 安装步骤
### 要安装stuoe，服务器必须具备以下条件
1. 安装Python3.8
2. 安装pypi依赖库
## 在此之前，您需要配置一些
##### 变更url.conf文件将的内容更改为网站的域名。即使使用反代理（例如nginx），此项也是必需的，因为在某些地方它是必需的
## 修改服务器配置，下面是一个例子
```python
{
'init':True,
'stuoe_name':'论坛的名字',
'stuoe_des':'关于你的论坛',
'stuoe_smtp_host':'SMTP服务器地址',
'stuoe_smtp_port':'SMTP服务器端口',
'stuoe_smtp_email':'SMTP服务器邮箱',
'stuoe_smtp_password':'SMTP服务器密码/授权码',
'stuoe_admin_mail':'管理员邮箱',
'stuoe_admin_password':'管理员密码',
'stuoe_themo_color':'DAF7A6'
}
```
### *或者你也可以选择用install界面来安装，保持init参数为False，运行stuoe.py，转到/install，输入配置信息，论坛就配置完成了!
