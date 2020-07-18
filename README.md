<div align="center">
<img src="https://raw.githubusercontent.com/snbck/stuoe.github.io/master/static/Stuoe.png" width="300" height="300">


[![license](https://img.shields.io/github/license/stuoe/stuoe.svg)](LICENSE)
[![Flask](https://img.shields.io/badge/%20power-Flask-blue.svg?style=flat-square)](https://github.com/pallets/flask)
![PyPI - Python](https://img.shields.io/badge/%20PYPI-stuoe-orange.svg?style=flat-square)
</div>

stuoe是一个轻量的论坛软件，为想要快速构建论坛的人准备的，即使是一个完全不懂技术的人也可以轻松的部署。不用配置数据库环境，因为他使用[Sqlite3]()。拥有丰富的扩展api.



## Installing
使用[pip](https://pypi.org)用于安装和更新


``` bash
pip install -U stuoe
```
## Fastest build
*在非生产环境下部署，如果在生产环境下请自行配置wsgi.py*

``` bash
stuoe startproject demo
cd demo
flask run
```

``` bash
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```
*尝试访问localhost:5000/install来配置和初始化论坛，如果这并不管用，请访问127.0.0.1/install，然后访问127.0.0.1/admin来设置论坛*

## Update Setup
*当版本更新时*

```bash
pip install -U stuoe
stuoe update --name demo
cd demo
flask db upgrade
flask run
```

## Components
*已有的组件列表*


* 安装界面
* 注册于登入
* 设置论坛的欢迎标题和横幅
* 对用户组分类
* 支持SMTP验证用户邮箱
* 使用富文本编辑器（支持上传图片）
* 使用标签对帖子分类
* 管理员对帖子顶置
* 管理员对帖子锁定
* 管理员发布帖子具有验证标志
* 一键设置论坛主题色
* 设置论坛头部js脚本
* 设置论坛 robots.txt
* 管理论坛标签（设置标题，图标）
* 用户设置个人介绍
* 用户默认哈希头像
* 用户上传自定义头像
* 用户对讨论加星标

*Stuoe在预览版中，你可以等待测试版，也可以与我们一起开发*



## Contact
* QQ 2731510961
* Email snbckcode@gmail.com
* Web [stuoe.cn](https://stuoe.cn)
* ORG [stuoe](https://github.com/stuoe)

## Contributor
*成员*
* [snbck](https://github.com/snbck)

*少数贡献者*   

* [shyfcka](https://github.com/shyfcka)
* [YDSzq](https://github.com/YDSzq)
* [Alex-hub79](https://github.com/Alex-hub79)


[Contributor](https://github.com/stuoe/stuoe/graphs/contributors)



## Link
* Web:  [https://stuoe.cn](https://stuoe.cn)
* Start: [https://stuoe.cn/docs/start.html](https://stuoe.cn/docs/start.html)
* Version : [https://pypi.org/project/stuoe](https://pypi.org/project/stuoe)
* discuss : [https://stuoe.pythonanywhere.com/](https://stuoe.pythonanywhere.com/)
