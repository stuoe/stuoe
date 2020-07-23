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
        return self.forum
