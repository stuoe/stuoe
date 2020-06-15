# Stuoe Start or Installing

from flask import *
import flask_mail
import os
import time

# Get Configs File
serverconf = dict(eval(open('server.conf', 'rb').read()))

# Check Server init State
if not serverconf['init']:
    pass