# Stuoe Start or Installing

from flask import *
from route import *
import flask_mail
import os
import time

# Get Configs File
serverconf = dict(eval(open('server.conf', 'rb').read()))

# Init Flask
app = Flask(__name__)

init_route(app)


@app.route('/install')
def installing_p():
    return ''

app.run(port=80, debug=True)
