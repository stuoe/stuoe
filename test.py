from flask import *
import os
app = Flask(__name__)

@app.route('/static/<path:path>')
def send_staticfile(path):
    if os.path.exists('staicfile/' + path):
        return open('staticfile/' + path,'rb').read()
    else:
        return abort(404)


@app.route('/userbyid/<userid:int>')
def send_user_by_id(userid):
    return 'defalt user'

@app.route('/userbyusername/<username:str>')
def send_user_by_id(username):
    return 'defalt user'


app.run()
