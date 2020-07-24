# Example - 示例插件

from flask import *
import os

# 插件头，标明插件的标题，图标，描述，README，
# 版本，作者等等信息


header = {
    "name": "example",
    "icon": "extension",
    "describe": "这个插件是为了方便介绍做如何制作插件的演示而制作的",
    "use": "some text",
    "author": "The Stuoe Project",
    "version": "0.0.1"
}

# 创建一个类，包含路由，绑定到app的方法,类名称不可变


class Main():
    # 获取Flask对象和SQLAlchemy对象
    def __init__(self, forum):
        self.forum = forum
    # 绑定这些路由,然后再将新的Flask对象归还

    def init(self,forum):

        app = forum.app_get_app()

        @app.route("/SNBCK_is_a_boy")
        def snbck_is_a_boy():
            return "Yes, that's right 😎"

        @app.route("/Is_SNBCK_a_boy/<boll>")
        def is_snbck_a_boy(boll):
            if boll == "yes":
                return "Yes, that's right 😎"
            else:
                return "Your answer is too bad 😒"
        forum.app_replace_app(app)

        return self.forum
