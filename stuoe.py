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
    if url == 'start':
        return open('backup/templates/installing/start.html','rb').read()
    elif url == 'database':
        return open('backup/templates/installing/database.html','rb').read()



app.run(port=80, debug=True)
