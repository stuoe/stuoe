# Stuoe Start or Installing

from flask import *
from flask_sqlalchemy import SQLAlchemy
import flask_mail
import os
import time
import jinja2

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
    user_des = db.Column(db.String(50))
    topic_list = db.Column(db.String(50))
    point = db.Column(db.Integer)
    url = db.Column(db.String(50))
    user_group = db.Column(db.Integer,db.ForeignKey("Group.Group_name"))
    user_ban = db.Column(db.Boolean)
    def __repr__(self):
           return {'id':self.id,'email':self.email,'user_des':self.user_des}
    
class Group(db.Model):
    # Waiting....
    Group_name = db.Column(db.String(30),primary_key=True)
    Group_des = db.Column(db.String(30))
    Highest_authority_group = db.Column(db.Boolean)
    group_user_info = db.relationship('User', back_populates='Group')

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
        serverconf['stuoe_admin_password'] = stuoe_admin_password
        serverconf['init'] = True



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

#@app.route('/install')
def send_vuejsindex():
    return open("storage/dist/installing.html",'rb').read()
    

app.run(port=80, debug=True)


