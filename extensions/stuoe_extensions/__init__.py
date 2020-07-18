import click

class Extensions():
    # 设置插件的基本信息
    def __init__(self,app,db):
        self.app = app
        self.db = db
    def add_route(self,url,function):
        self.app.add_url_rule(url,view_func=function)
        print("增加路由" + url)
