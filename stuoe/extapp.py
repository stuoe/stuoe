# Stuoe在初始化时会调用init()函数来导入所有插件,
# 通过遍历文件夹来找到每个插件的__init__.py,传入app
# 和db对象，将路由添加到app.


import os
import importlib

# 指定导入方式，目前只有all
importype = 'all'


def init(app, db):
    for i in os.listdir("extension"):
        print("导入模块: " + i)
        theExtensions = importlib.import_module("extension." + i + ".main")
        app = theExtensions.Main(app,db).init()
    return app       

