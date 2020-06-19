# Stuoe Start or Installing

from flask import *
from flask_sqlalchemy import SQLAlchemy
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

# Get Configs File
serverconf = dict(eval(open('server.conf', 'rb').read()))
serverurl = open('url.conf', 'rb').read()

# Init Flask
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///stuoe.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.config['MAIL_SERVER'] = serverconf['stuoe_smtp_host']
app.config['MAIL_PORT'] = int(serverconf['stuoe_smtp_port'])
app.config['MAIL_USERNAME'] = serverconf['stuoe_smtp_email']
app.config['MAIL_PASSWORD'] = serverconf['stuoe_smtp_password']
app.config['MAIL_USE_SSL']=True

db = SQLAlchemy(app)
mail = flask_mail.Mail(app)

# Init DatabaseTable

class User(db.Model):
    __tablename__ = 'User'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(50))
    pass_hash = db.Column(db.String(50))
    user_des = db.Column(db.String(50), server_default='该用户还什么都没写呢')
    user_session = db.Column(db.String(50), server_default='None')
    point = db.Column(db.Integer, server_default='1')
    url = db.Column(db.String(50), server_default='not url')
    user_group = db.Column(db.Integer, db.ForeignKey("Group.Group_name"))
    user_ban = db.Column(db.Boolean, server_default='False')
    user_dirty = db.Column(db.Boolean, server_default='False')
    def __repr__(self):
        return {'id': self.id, 'email': self.email, 'user_des': self.user_des}


class Group(db.Model):
    # Waiting....
    __tablename__ = 'Group'
    Group_name = db.Column(db.String(30), primary_key=True)
    Group_des = db.Column(db.String(30), server_default='此分组还没有描述')
    Highest_authority_group = db.Column(db.Boolean, server_default='True')

    def __repr__(self):
        return self.Group_name

class Discussion(db.Model):
    # Waiting...
    __tablename__ = 'Discussion'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    Discussion_title = db.Column(db.String(30))
    Discussion_body_text = db.Column(db.String(60000))
    Discussion_Publisher = db.Column(db.Integer, db.ForeignKey("User.id"))
    Discussion_watch_user = db.Column(db.Integer, db.ForeignKey("User.id"))
    Discussion_star_user = db.Column(db.Integer, db.ForeignKey("User.id"))
    Discussion_Private_in_Publisher = db.Column(db.Boolean, server_default='False')
    Discussion_Private_in_group = db.Column(db.Boolean, server_default='False')
    Discussion_Private_in_bbs = db.Column(db.Boolean, server_default='False')
    Discussion_No_discussion = db.Column(db.Boolean, server_default='False')
    Discussion_lock_up = db.Column(db.Boolean, server_default='False')
    Discussion_high_quality = db.Column(db.Boolean, server_default='False')
    Discussion_some_son = db.Column(db.Boolean, server_default='False')

class Discussion_son(db.Model):
    # Waiting...
    __tablename__ = 'Discussion_son'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    Discussion_son_Publisher = db.Column(db.Integer, db.ForeignKey("User.id"))
    Discussion_son_body_text = db.Column(db.String(60000))
    



db.create_all()

# Install

@app.route('/install')
def send_redict():
    if serverconf['init']:
        return abort(403)
    return open('storage\dist\index.html', 'rb').read()


@app.route('/install/start', methods=['GET', 'POST'])
def installing_step():
    if serverconf['init']:
        return abort(403)
    if request.method == "POST":
        stuoe_name = request.form['stuoe_name']
        stuoe_des = request.form['stuoe_des']
        stuoe_smtp_host = request.form['stuoe_smtp_host']
        stuoe_smtp_host = request.form['stuoe_smtp_port']
        stuoe_smtp_email = request.form['stuoe_smtp_port']
        stuoe_smtp_password = request.form['stuoe_smtp_email']
        stuoe_admin_mail = request.form['stuoe_admin_mail']
        stuoe_admin_password = request.form['stuoe_admin_password']
        if stuoe_name == '':
            return open('storage\stuoe\public\install_error.html', 'rb').read()
        if stuoe_des == '':
            return open('storage\stuoe\public\install_error.html', 'rb').read()
        serverconf['stuoe_name'] = stuoe_name
        serverconf['stuoe_des'] = stuoe_des
        serevrconf['stuoe_smtp_host'] = stuoe_smtp_host
        serverconf['stuoe_smtp_port'] = stuoe_smtp_port
        serverconf['stuoe_smtp_email'] = stuoe_smtp_email
        serverconf['stuoe_smtp_password'] = stuoe_admin_password
        sevrerconf['stuoe_admin_mail'] = stuoe_admin_mail
        serverconf['init'] = True

        admin_passhash_byhash256 = hashlib.sha256(
            stuoe_admin_password.encode('utf-8'))
        admin = User(email=serverconf['stuoe_admin_mail'],
                     passhash=admin_passhash_byhash256)
        Register_user_group = Group(Group_name='注册用户组',Group_des='注册用户组，享有普通权限，例如发帖，回复等')
        db.session.add(admin)
        db.session.add(Register_user_group)
        db.session.commit()
        open('serverconf', 'wb+').write(str(serverconf).encode('utf-8'))
        return redirect('/')
    else:
        return redirect('/install')

# Router
@app.route('/')
def send_index():
    return open('storage\dist\home.html', 'rb').read()

# Staticfile


@app.route('/js/<path:path>')
def send_jsfile(path):
    if os.path.exists("storage/dist/js/" + path):
        return open("storage/dist/js/" + path, 'rb').read()
    else:
        return abort(404)


@app.route('/css/<path:path>')
def send_cssfile(path):

    if os.path.exists("storage/dist/css/" + path):
        resp = make_response(open("storage/dist/css/" + path, 'rb').read())
        resp.headers["Content-Type"] = 'text/css'
        return resp
    else:
        return abort(404)


@app.route('/favicon.ico')
def send_ico():
    return open("storage/dist/图标.ico", 'rb').read()

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
    request.form['register_email']
    request.form['register_password']
    if not re.match("^.+\\@(\\[?)[a-zA-Z0-9\\-\\.]+\\.([a-zA-Z]{2,3}|[0-9]{1,3})(\\]?)$", request.form['register_email']) != None:
        return '502'
    if request.form['register_password'] == '':
        return '502'
    if not User.query.filter_by(email=request.form['register_email']).first() == None:
        return 'Email_repeat'
    key = hashlib.sha3_256(str(os.urandom(3600)).encode('utf-8'))
    p = random.randint(10000,999999)
    verify_registered_email.append({
        'key': key.hexdigest(),
        'hash_url': p,
        'email': request.form['register_email'],
        'password': request.form['register_email']})

    msg = flask_mail.Message('[' + serverconf['stuoe_name'] + ']', sender=serverconf['stuoe_smtp_email'],
            recipients=[request.form['register_email']])
    msg.body = '邮件验证码'
    msg.html = '<b>你正在注册{{name}}</b><br><h4>验证码:{p}</h4>'.format(name=serverconf['stuoe_name'],p=p)
    send_mail(msg)
    return key.hexdigest()

@app.route('/api/check_code_for_register',methods=['POST'])
def send_api_check_emailcode():
    request.form['key']
    request.form['code']
    register_email = ''
    for i in verify_registered_email:
        if request.form['code'] == i['key']:
            if i['hash_url'] == request.form['code']:
                request_email = i['email']
                break
    if register_email == '':
        return '502'
    
    return 'register_ok'



def send_mail(msg):
    threading._start_new_thread(mail.send,(msg,))

app.run(port=31, debug=True)
