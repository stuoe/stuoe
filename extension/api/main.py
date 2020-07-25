

from flask import *
import os



header = {
    "name": "autoAPI",
    "icon": "web_asset",
    "describe": "为论坛增加api功能",
    "use": "阅读文档",
    "author": "The Stuoe Project",
    "version": "0.0.1"
}

class Main():
    def __init__(self, forum):
        self.forum = forum

    def init(self,forum):
        return self.forum
