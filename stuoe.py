# Stuoe Start or Installing

from flask import *
from flask_sqlalchemy import SQLAlchemy
import view
import flask_mail
import flask_oauthlib
import os
import time
import jinja2
import hashlib
import re
import random
import threading

# Global Var
verify_registered_email = list()
online_user = list()
avater = open

# Get Configs File
serverconf = dict(eval(open('server.conf', 'rb').read()))
serverurl = serverconf['url']
# Init Flask
app = Flask(__name__, static_url_path='/static', static_folder='public')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sqlite3.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.config['MAIL_SERVER'] = serverconf['stuoe_smtp_host']
app.config['MAIL_PORT'] = int(serverconf['stuoe_smtp_port'])
app.config['MAIL_USERNAME'] = serverconf['stuoe_smtp_email']
app.config['MAIL_PASSWORD'] = serverconf['stuoe_smtp_password']
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_DEFAULT_SENDER'] = serverconf['stuoe_smtp_email']
app.config['SECRET_KEY'] = os.urandom(20)

# Init View
Viewrender = view


# Init DatabaseTable , Email , function
db = SQLAlchemy(app)
mail = flask_mail.Mail(app)


class User(db.Model):
    __tablename__ = 'User'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(50))
    verify_email = db.Column(db.Boolean, server_default='False')
    passhash = db.Column(db.String(50))
    nickname = db.Column(db.String(50))
    user_des = db.Column(
        db.String(50),
        server_default='Wait....And Something Text About This User')
    user_session = db.Column(db.String(50), server_default='None')
    point = db.Column(db.Integer, server_default='1')
    url = db.Column(db.String(50), server_default='not url')
    user_group = db.Column(db.Integer, db.ForeignKey("Group.Group_name"))
    user_ban = db.Column(db.Boolean, server_default='False')
    user_dirty = db.Column(db.Boolean, server_default='False')
    registertime = db.Column(db.Integer)
    pushingPost = db.relationship("Post",backref="User")
    MessageToMailbox = db.Column(db.Boolean, server_default='True')
    UserMessageMainbox = db.relationship("Messages",backref="User")

    def __repr__(self):
        return {'id': self.id, 'email': self.email, 'user_des': self.user_des}


class Group(db.Model):
    # Waiting....
    __tablename__ = 'Group'
    Group_name = db.Column(db.String(30), primary_key=True)
    Group_des = db.Column(db.String(30), server_default='此分组还没有描述')
    Highest_authority_group = db.Column(db.Boolean, server_default='False')
    user = db.relationship("User",backref="Group")

    def __repr__(self):
        return self.Group_name


class File(db.Model):
    __tablename__ = 'File'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)


class Post(db.Model):
    __tablename__ = 'Post'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    pusher = db.Column(db.String(40), db.ForeignKey('User.id'))
    title = db.Column(db.String(50))
    body = db.Column(db.String(2000000))
    pushingtime = db.Column(db.Integer)
    tags = db.Column(db.String(40), db.ForeignKey('Tags.id'))


class Messages(db.Model):
    __tablename__ = 'Messages'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    subject = db.Column(db.String(50))
    body = db.Column(db.String(3000))
    PostTime = db.Column(db.Integer)
    Postman = db.Column(db.String(40), db.ForeignKey('User.id'))

class Tags(db.Model):
    __tablename__ = 'Tags'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(30),server_default='Hashing')
    post = db.relationship("Post",backref="Tags")
    lock = db.Column(db.Boolean, server_default='False')
    icon = db.Column(db.String(30),server_defalt='message')



db.create_all()

# Check whether two groups are created

if Group.query.filter_by(Group_name='注册用户').first() is None:
    RegisterGourp = Group(
        Group_name='注册用户', Group_des="普通的注册用户", Highest_authority_group=False)
    db.session.add(RegisterGourp)
    db.session.flush()
    db.session.commit()
if Group.query.filter_by(Group_name='管理员').first() is None:
    AdminGourp = Group(
        Group_name='管理员',
        Group_des="维持论坛秩序，论坛所有者或者所有者的协助者",
        Highest_authority_group=True)
    db.session.add(AdminGourp)
    db.session.commit()
if Tags.query.filter_by(name="新鲜事").first() is None:
    goodnewsTags = Tags(name='新鲜事',lock=False,icon='message')
    db.session.add(goodnewsTags)
    db.session.flush()
    db.session.commit()
if Tags.query.filter_by(name="咕咚事").first() is None:
    goodnewsTags = Tags(name='咕咚事',lock=False,icon='child_care')
    db.session.add(goodnewsTags)
    db.session.flush()
    db.session.commit()
    
# function


def db_getuserByemail(email):
    return User.query.filter_by(email=email).first()

def db_getuserByid(id):
    return User.query.filter_by(id=id).first()

def db_getpostByid(id):
    return Post.query.filter_by(id=id).first()

def db_gettagsByname(name):
    return Tags.query.filter_by(name=name).first()

def db_getGroupByid(name):
    return Group.query.filter_by(name=name).first()


def db_check_repeat_email(email):
    if User.query.filter_by(email=email).first() is None:
        return True
    else:
        return False


def db_create_user(email, password, nickname, user_group):
    if not db_check_repeat_email(email):
        return False
    new_user = User(
        email=email,
        verify_email=False,
        passhash=hashlib.sha256(
            password.encode('utf-8')).hexdigest(),
        nickname=nickname,
        user_des='Wait....And Something Text About This User',
        user_session='',
        point='1',
        url='',
        user_group=user_group,
        user_ban=False,
        user_dirty=False,
        registertime=time.time(),
        MessageToMailbox=True)
    db.session.add(new_user)
    db.session.flush()
    db.session.commit()
    db_set_user_session(new_user.id)


def db_set_user_session(id):
    obj = db_getuserByid(id)
    if obj is not None:
        session_random = hashlib.sha256(
            str(random.randint(0, 300000)).encode('utf-8')).hexdigest()
        obj.user_session = session_random
        session['id'] = id
        session['key'] = session_random
        db.session.flush()
        db.session.commit()
        return session_random
    return False


def get_session(type='nickname'):
    if session.get('id') is None or session.get('key') is None:
        session.clear()
        return False
    obj = db_getuserByid(session.get('id'))
    if obj is None:
        return False
    if obj.user_session == session.get('key'):
        if type == 'nickname':
            return obj.nickname
        elif type == 'id':
            return obj.id
        elif type == 'obj':
            return obj

    else:
        session.clear()


# Install


@app.route('/install')
def send_redict():
    if serverconf['init']:
        return abort(403)
    a = open('storage/templates/install/index.html',
             'r', encoding='utf-8').read()
    m = jinja2.Template(str(a))
    return m.render(
        name=serverconf['stuoe_name'],
        smtp_host=serverconf['stuoe_smtp_host'],
        smtp_port=serverconf['stuoe_smtp_port'],
        smtp_email=serverconf['stuoe_smtp_email'],
        smtp_password=serverconf['stuoe_smtp_password'],
        admin_mail=serverconf['stuoe_admin_mail'],
        admin_password=serverconf['stuoe_admin_password'])


@app.route('/install/start', methods=['GET', 'POST'])
def installing_step():
    if serverconf['init']:
        return abort(403)
    if request.method == "POST":
        stuoe_name = request.form['stuoe_name']
        stuoe_smtp_host = request.form['stuoe_smtp_host']
        stuoe_smtp_port = request.form['stuoe_smtp_port']
        stuoe_smtp_email = request.form['stuoe_smtp_email']
        stuoe_smtp_password = request.form['stuoe_smtp_password']
        stuoe_admin_mail = request.form['stuoe_admin_mail']
        stuoe_admin_password = request.form['stuoe_admin_password']
        if stuoe_name == '':
            return open(
                r'storage\stuoe\public\install_error.html',
                'rb').read()
        serverconf['stuoe_name'] = stuoe_name
        serverconf['stuoe_des'] = stuoe_name
        serverconf['stuoe_smtp_host'] = stuoe_smtp_host
        serverconf['stuoe_smtp_port'] = stuoe_smtp_port
        serverconf['stuoe_smtp_email'] = stuoe_smtp_email
        serverconf['stuoe_smtp_password'] = "Action"
        serverconf['stuoe_admin_mail'] = stuoe_admin_mail
        serverconf['stuoe_admin_password'] = stuoe_admin_password
        serverconf['init'] = True

        db_create_user(stuoe_admin_mail, stuoe_admin_password, 'Admin', '管理员')
        open('server.conf', 'wb+').write(str(serverconf).encode('utf-8'))
        return redirect('/')
    else:
        return redirect('/install')

# Router


@app.route('/')
def send_index():
    if get_session() == False:
        return Viewrender.gethome(auth=False)
    else:
        return Viewrender.gethome(auth=True, userObj=get_session('obj'))


@app.route('/logout')
def user_logout():
    session.clear()
    return redirect('/')


@app.route('/u/<uid>')
def user_space(uid):
    obj = db_getuserByid(uid)
    if obj is None:
        return abort(404)
    user = get_session('obj')
    if not user:
        return Viewrender.getUserSpace(auth=False, lookuserObj=obj)
    else:
        return Viewrender.getUserSpace(
            auth=True, lookuserObj=obj, userObj=user)

@app.route('/p/<pid>')
def post_pages(pid):
    obj = db_getpostByid(pid)
    if obj is None:
        return abort(404)
    user = get_session('obj')
    pusherUser = db_getuserByid(obj.pusher)
    postTags = db_gettagsByname(obj.tags)
    if not user:
        return Viewrender.getPost(auth=False,pusherUserObj=pusherUser,Post=obj,Tags=postTags)
    else:
        return Viewrender.getPost(auth=True,pusherUserObj=pusherUser,Post=obj,Tags=postTags,userObj=user)

    
@app.route('/write')
def write_index():
    if get_session() == False:
        return Viewrender.getWrite(auth=False,Tags=Tags.query.all())
    else:

        return Viewrender.getWrite(auth=True, userObj=get_session(type="obj"),Tags=Tags.query.all())


@app.route('/settings')
def user_settings():
    if get_session() == False:
        return abort(403)
    return Viewrender.getSettings(get_session(type='obj'))


@app.route('/settings/profile', methods=['POST'])
def user_changsettings_profile():
    user = get_session('obj')
    if not user:
        return abort(403)
    request.form['nickname']
    request.form['user_des']
    request.form['url']
    if request.form == '':
        return Viewrender.getMSG('昵称不能为空', auth=True, userObj=user)
    user.nickname = request.form['nickname']
    user.user_des = request.form['user_des']
    user.url = request.form['url']
    db.session.flush()
    db.session.commit()
    return redirect('/settings')


@app.route('/settings/email', methods=['POST'])
def user_changsettings_email():
    user = get_session('obj')
    if not user:
        return abort(403)
    request.form['email']
    if not re.match(
        "^.+\\@(\\[?)[a-zA-Z0-9\\-\\.]+\\.([a-zA-Z]{2,3}|[0-9]{1,3})(\\]?)$",
            request.form['email']) is not None:
        return Viewrender.getMSG('请填写正确的邮箱',auth=True,userObj=user)
    action = Viewrender.renderEmailCheckMessages(user, request.form['email'])
    msg = flask_mail.Message(recipients=[request.form['email']],
                             html=action['msg'],
                             subject='更改邮箱',)
    threading._start_new_thread(send_mail,(msg,))
    verify_registered_email.append({
        "userObj": user,
        "code": action['code'],
        "email": request.form['email']
    })
    return redirect('/settings/check')


@app.route('/settings/check', methods=['GET', 'POST'])
def user_changsettings_checkemail():
    user = get_session('obj')
    if not user:
        return abort(403)
    if request.method == 'GET':
        return Viewrender.getCheck(user)
    request.form['code']
    for i in verify_registered_email:
        if i['userObj'].id == user.id:
            if request.form['code'] == i['code']:
                user.email = i['email']
                user.verify_email = True
                db.session.flush()
                db.session.commit()
                return Viewrender.getMSG("设置成功",auth=True,userObj=user)
            else:
                return Viewrender.getMSG("验证码不正确",auth=True,userObj=user)
    return Viewrender.getMSG('该用户并未发起更改邮件事务,找不到对象',auth=True,userObj=user)


# Staticfile

# None  Other StaticFile


@app.route('/stuoe.css')
def send_css():
    return open('storage/static/stuoe/stuoe.css', 'rb').read()

# API interface area


@app.route('/api/configs', methods=['GET'])
def send_api_configs():
    serverconf = dict(eval(open('server.conf', 'rb').read()))
    return str({
        'stuoe_name': serverconf['stuoe_name'],
        'stuoe_des': serverconf['stuoe_des'],
        'stuoe_themo_color': serverconf['stuoe_themo_color']
    })


@app.route('/api/register', methods=['POST'])
def send_api_register():
    request.form['nickname']
    request.form['email']
    request.form['password']
    if not re.match(
        "^.+\\@(\\[?)[a-zA-Z0-9\\-\\.]+\\.([a-zA-Z]{2,3}|[0-9]{1,3})(\\]?)$",
            request.form['email']) is not None:
        return Viewrender.getMSG('请填写正确的邮箱')
    if request.form['email'] == '':
        return Viewrender.getMSG('请填写完整的信息')
    if request.form['password'] == '':
        return Viewrender.getMSG('请填写完整的信息')
    if not User.query.filter_by(email=request.form['email']).first() is None:
        return Viewrender.getMSG('此邮箱已被注册')
    db_create_user(
        email=request.form['email'],
        password=request.form['password'],
        nickname=request.form['nickname'],
        user_group='普通用户')
    return redirect('/')


@app.route('/api/login', methods=['POST'])
def send_api_login():
    request.form['email']
    request.form['password']
    if request.form['email'] == '' or request.form['password'] == '':
        return Viewrender.getMSG('请填写完整信息')
    obj = db_getuserByemail(request.form['email'])
    if obj is None:
        return Viewrender.getMSG('没有匹配的用户')
    passhash = hashlib.sha256(
        request.form['password'].encode('utf-8')).hexdigest()
    if obj.passhash == passhash:
        db_set_user_session(obj.id)
        return redirect('/')
    else:
        return Viewrender.getMSG('账号或者密码不正确')

@app.route('/postwrite',methods=['POST'])
def pushing_post():
    user = get_session('obj')
    if not user:
        return abort(403)
    request.form['title']
    request.form['tags']
    request.form['body']
    if request.form['title'] == '' or request.form['tags'] == '' or request.form['body'] == '':
        return Viewrender.getMSG('请填写完善标题，标签，正文',user)
    pickerInListBool =  False
    for tags in Tags.query.all():
        if tags.name == request.form['tags'] and tags.lock==False:
            pickerInListBool = True
            break
    if not pickerInListBool:
        return Viewrender.getMSG('标签不存在或已被管理员关闭讨论',user)
    if not user.verify_email:
        return Viewrender.getMSG('该用户并未验证邮箱，无权限发布讨论',user)
    if user.user_ban:
        return Viewrender.getMSG('该用户发布讨论权限已被禁用，请联系管理员',user)
    newPost = Post(pusher=user.id,title=request.form['title'],body=request.form['body'],pushingtime=time.time(),tags=request.form['tags'])
    db.session.add(newPost)
    db.session.flush()
    db.session.commit()
    return redirect('/p/' + str(newPost.id))


def send_mail(msg):
    with app.app_context():
        mail.send(msg)


app.run(host='0.0.0.0', port=3000)

