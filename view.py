import jinja2


# Get Configs File
serverconf = dict(eval(open('server.conf', 'rb').read()))
serverurl = serverconf['url']

def getTemplates():
    nav = jinja2.Template(open('storage/templates/nav/nouser.html','r',encoding="utf-8").read()).render(title=serverconf['stuoe_name'])
    return jinja2.Template(open('storage/templates/base.html', 'r',encoding="utf-8").read()).render(title=serverconf['stuoe_name'],nav=nav,body='')

def gethome():
    return getTemplates()