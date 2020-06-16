# Stuoe Start or Installing

from flask import *
import flask_mail
import os
import time

# Get Configs File
serverconf = dict(eval(open('server.conf', 'rb').read()))

# Init Flask
app = Flask(__name__)


@app.route('/install')
def installing_p():
    return redirect('/install/start')

@app.route('/install/<url>',methods=['GET','POST'])
def installing_step(url):
    if serverconf['init']:
        return abort(403)
    if url == 'start' and request.method=="POST":
        serverconf['info']['stuoe_name'] = request.form['fourm_name']
        serverconf['info']['des'] = request.form['fourm_admin_email']
        serverconf['info']['fourm_des'] = request.form['fourm_des']
        open('serverconf','wb+').write(str(serverconf).encode('utf-8'))
        return redirect('/install/database')

    elif url == 'smtp' and request.method=="POST":
        serverconf['info']['stuoe_name'] = request.form['fourm_name']
        serverconf['info']['des'] = request.form['fourm_admin_email']
        serverconf['info']['fourm_des'] = request.form['fourm_des']
        open('serverconf','wb+').write(str(serverconf).encode('utf-8'))
        return redirect('/install/installing')
    elif url == "start" and request.method=="GET":
        return open('/storage/dist/installing/start.html','rb').read()
    elif url == "database" and request.method=="GET":
        return open('/storage/dist/installing/database.html','rb').read()
    elif url == "smtp" and request.method=="GET":
        return open('/storage/dist/installing/smtp.html','rb').read()

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

@app.route('/')
def send_vuejsindex():
    return open("storage/dist/index.html",'rb').read()
    

app.run(port=80, debug=True)


