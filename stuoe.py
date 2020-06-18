# Stuoe Start or Installing

from flask import *
from flask_sqlalchemy import SQLAlchemy
import flask_mail
import os
import time
import jinja2
import hashlib

# Get Configs File
serverconf = dict(eval(open('server.conf', 'rb').read()))

# Init Flask
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///stuoe.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
db = SQLAlchemy(app)

# Init DatabaseTable
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(50))
    pass_hash = db.Column(db.String(50))
    user_des = db.Column(db.String(50),server_default='该用户还什么都没写呢')
    point = db.Column(db.Integer,server_default='1')
    url = db.Column(db.String(50),server_default='not url')
    user_group = db.relationship('Group',backref='User')
    user_ban = db.Column(db.Boolean,server_default='False')
    def __repr__(self):
           return {'id':self.id,'email':self.email,'user_des':self.user_des}
    
class Group(db.Model):
    # Waiting....
    Group_name = db.Column(db.String(30),primary_key=True)
    Group_des = db.Column(db.String(30),server_default='此分组还没有描述')
    Highest_authority_group = db.Column(db.Boolean,server_default='True')
    group_user_info = db.relationship("User", back_populates="Group")
    def __repr__(self):
        return self.Group_name

db.create_all()

@app.route('/install')
def send_redict():
    return open('storage\stuoe\public\index.html','rb').read()

@app.route('/install',methods=['GET','POST'])
def installing_step(url):
    if serverconf['init']:
        return abort(403)
    if request.method=="POST":
        stuoe_name = request.form['stuoe_name']
        stuoe_des = request.form['stuoe_des']
        stuoe_smtp_host = request.form['stuoe_smtp_host']
        stuoe_smtp_host = request.form['stuoe_smtp_port']
        stuoe_smtp_email = request.form['stuoe_smtp_port']
        stuoe_smtp_password = request.form['stuoe_smtp_email']
        stuoe_admin_mail = request.form['stuoe_admin_mail']
        stuoe_admin_password = request.form['stuoe_admin_password']
        if stuoe_name == '':
            return open('storage\stuoe\public\install_error.html','rb').read()
        if stuoe_des == '':
            return open('storage\stuoe\public\install_error.html','rb').read()
        serverconf['stuoe_name'] = stuoe_name
        serverconf['stuoe_des'] = stuoe_des
        serevrconf['stuoe_smtp_host'] = stuoe_smtp_host
        serverconf['stuoe_smtp_port'] = stuoe_smtp_port
        serverconf['stuoe_smtp_email'] = stuoe_smtp_email
        serverconf['stuoe_smtp_password'] = stuoe_admin_password
        sevrerconf['stuoe_admin_mail'] = stuoe_admin_mail
        serverconf['init'] = True

        admin_passhash_byhash256 = hashlib.sha256(stuoe_admin_password.encode('utf-8'))
        admin = User(email=serverconf['stuoe_admin_mail'],passhash=admin_passhash_byhash256)
        db.session.add(admin)
        db.session.commit()
        open('serverconf','wb+').write(str(serverconf).encode('utf-8'))
        return redirect('/install/database')
    else:
        return open('storage\stuoe\public\start.html','rb').read()


        

@app.route('/js/<path:path>')
def send_jsfile(path):
    if os.path.exists("storage/dist/js/" + path):
        return open("storage/dist/js/" + path,'rb').read()
    else:
        return abort(404)

@app.route('/css/<path:path>')
def send_cssfile(path):
    if os.path.exists("storage/dist/css/" + path):
        return open("storage/dist/css/" + path,'rb').read()
    else:
        return abort(404)

# API interface area

@app.route('/api/configs',methods=['GET'])
def send_api_configs():
    serverconf = dict(eval(open('server.conf', 'rb').read()))
    return str({
        'stuoe_name':serverconf['stuoe_name'],
        'stuoe_des':serverconf['stuoe_des'],
        'stuoe_themo_color':serverconf['stuoe_themo_color']
    })

@app.route('/api/regsiter',methods=['POST'])
def send_api_register():
    pass


    

app.run(port=80, debug=True)


