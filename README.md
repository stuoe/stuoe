# Stuoe Framework 🍦

Stuoe Framework是一个面向于想要快速构建论坛的新手和开发者的论坛框架。本身基于Python，界面使用MDUI，使用Jinja2来加速渲染界面。最基本的标签，回复，提到，富文本编辑器，等等功能都能胜任。拥有丰富的api进行开发，以及个性化主题.

## Install

``` bash
git clone https://github.com/stuoe/stuoe.git
cd stuoe
```
或者在码云下载
``` bash
https://gitee.com/stuoe/stuoe.git
cd stuoe
```

## Usage

使用Stuoe Framework需要部署的环境少之又少
1. Python3.8+以及扩展
2. Nginx+uWsgi（在生产中使用）



先安装依赖的Python扩展
``` bash
pip install -r requirements.txt
```
环境没问题的话直接运行（启动时间较长，4-7秒)
``` bash
python stuoe.py
```
输出类似以下
``` bash
 * Serving Flask app "stuoe" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Restarting with windowsapi reloader
 * Debugger is active!
 * Debugger PIN: 190-981-669
 * Running on http://0.0.0.0:31/ (Press CTRL+C to quit)
```
现在在浏览器输入127.0.0.1:31/install就可以访问安装界面，如果运行失败请检查环境和依赖扩展，端口是否被占用，权限是否到位等等

目前的Stuoe Framework通过Werkzeug进行部署，无法承受太多的并发和请求，并且部署也并不持久，所以需要使用Nginx + uWSGI（反代理+Web容器）进行部署



## Contributing

Stuoe Framework由一群热爱技术的学生开发（11-16岁）

## License

开源项目遵循[Apache License Version 2.0](http://www.apache.org/licenses/)，使用和修改请参照说明，尊重代码作者的著作权

