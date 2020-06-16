from flask import *
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)



app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config['SQLALCHEMY_ECHO'] = True

serverconf = dict(eval(open('server.conf', 'rb').read()))


class Configs():
    def __init__(self):
        self.host = serverconf['database']['host']
        self.port = '3306'
        self.database_name = 'csdn'
        self.database_user = 'csdn'
        self.database_password = 'pcPTpJMWLSHnGtcn'
        # 这个是数据库上的连接地址
        self.database_url = "mysql+pymysql://{database_user}:{database_password}@{host}:{port}/{database_name}?charset=utf8".format(database_user=self.database_user, database_password=self.database_password, host=self.host, port=self.port, database_name=self.database_name)


# 配置数据库地址
app.config['SQLALCHEMY_DATABASE_URI'] = Configs().database_url

# 优雅的数据库对象
db_obj = SQLAlchemy(app)
db_obj.init_app(app)

# 定义第一个模型


class Text(db_obj.Model):
    # 设置表名，如果不定义就默认为类名
    __tablename__ = "Text"

    # db.Column是定义列（就是表中的每个模型的属性）,primary_key属性是设置定位key，例如id
    id = db_obj.Column(db_obj.Integer, primary_key=True)
    text = db_obj.Column(db_obj.String(72))
    


# 将所有的表添加的数据库中
db_obj.create_all()
