# Stuoe Framework 0.1.2预览版

Stuoe Framework是一个面向于想要快速构建论坛的新手和开发者的论坛框架。本身基于Python，界面使用MDUI，使用Jinja2来加速渲染界面。最基本的标签，回复，提到，富文本编辑器，等等功能都能胜任。拥有丰富的api进行开发，以及个性化主题.

* 使用Python，因此他很容易安装。使用Sqlite3，不用安装数据库环境
* 界面美观，不臃肿.Jinja2渲染，快速
* 开源，数据透明。开源协议：[Apach License](http://www.apache.org/licenses/)


> Stuoe目前正在预览版中，有太多的功能没有实现，所以并不代表最终品质

>如果你愿意与我们一起开发Stuoe，可以发邮件到snbckcode@gmail.com

## Usage
使用pip安装命令行工具
``` bash
pip install stuoe
```
或者使用easy_install
``` bash
easy_install install stuoe
```
新建一个项目工程
``` bash
stuoe startproject --name demobbs
cd demobbs
```
运行它
``` bash
flask run
```

更多资料:stuoe.cn（开发中）

## License

Apach License

## Link

官网 https://stuoe.cn

开发者论坛 https://stuoe.pythonanywhere.com/p/1

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/stuoe/stuoe)
