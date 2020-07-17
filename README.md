<div align="center">
<img src="https://cdn.jsdelivr.net/gh/stuoe/stuoe.github.io@master/static/Stuoe.png" width="300" height="300">


[![license](https://img.shields.io/github/license/stuoe/stuoe.svg)](LICENSE)
[![Flask](https://img.shields.io/badge/%20power-Flask-blue.svg?style=flat-square)](https://github.com/pallets/flask)
![PyPI - Python](https://img.shields.io/badge/%20PYPI-stuoe-orange.svg?style=flat-square)
</div>

stuoe是一个轻量的论坛软件，为想要快速构建论坛的人准备的，即使是一个完全不懂技术的人也可以轻松的部署。不用配置数据库环境，因为他使用[Sqlite3]()。拥有丰富的扩展api.

Stuoe is a lightweight forum software for people who want to build a forum quickly. Even a person who doesn't know technology can easily deploy it. There is no need to configure the database environment because it uses [SQLite3](). It has rich extension API

## Installing
使用[pip](https://pypi.org)用于安装和更新

Use [pip](https://pypi.org)  For installation and updates

``` bash
pip install -U stuoe
```
## Fastest build
*(nonproductive)*

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
*Add / admin on the route to initialize the forum*

## Update Setup
*When the version is updated*

```bash
pip install -U stuoe
stuoe update --name demo
cd demo
flask db upgrade
flask run
```

## Components
*List of completed components*


* Installation interface
* Registration and login
* Set up personal information and view activities on your home page
* Classification of user groups
* Use SMTP to verify mailbox
* Rich text editor
* Use tags to categorize posts
* Independent label display interface
* The administrator can top the post
* Administrators can lock posts (no discussion)
* Posts posted by administrators have a validation icon
* Reply to the post
* Use stars for posts
* Search the whole station
* Overview of forum data
* Set the title and banner of the forum
* Set forum theme colors (19 kinds)
* Setting up Forum robots.txt
* Set the JS script in the forum header
* Add Google statistics
* Manage forum tags (set title, set icon)

*Stuoe is still in the preview version, there are too many deficiencies to be improved. You can wait for the beta version, or you can join us in the development*



## Contact
* QQ 2731510961
* Email snbckcode@gmail.com
* Web [stuoe.cn](https://stuoe.cn)
* ORG [stuoe](https://github.com/stuoe)

## Contributor
*Key contributors*
* [snbck](https://github.com/snbck)
* [shyfcka](https://github.com/shyfcka)
* [YDSzq](https://github.com/YDSzq)
* [Alex-hub79](https://github.com/Alex-hub79)

*The ranking is statistically ranked by GitHub. For more information, please refer to: [Contributor](https://github.com/stuoe/stuoe/graphs/contributors)*


*If you want to [pull requests](https://github.com/pulls), the code should be written in accordance with [PEP8](https://www.python.org/dev/peps/pep-0008/), with appropriate comments and clear remarks. HTML file, please format*

## Link
* Web:  [https://stuoe.cn](https://stuoe.cn)
* Start: [https://stuoe.cn/docs/start.html](https://stuoe.cn/docs/start.html)
* Version : [https://pypi.org/project/stuoe](https://pypi.org/project/stuoe)
* discuss : [https://stuoe.pythonanywhere.com/](https://stuoe.pythonanywhere.com/)
