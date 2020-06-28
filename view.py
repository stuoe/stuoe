import jinja2


# Get Configs File
serverconf = dict(eval(open('server.conf', 'rb').read()))
serverurl = serverconf['url']

# And Base Templates



def getTemplates(body='',auth=False,nickname='Nickname'):
    if auth:
         nav = jinja2.Template(open('storage/templates/nav/user.html','r',encoding="utf-8").read()).render(title=serverconf['stuoe_name'],nickname=nickname)
    else:
         nav = jinja2.Template(open('storage/templates/nav/nouser.html','r',encoding="utf-8").read()).render(title=serverconf['stuoe_name'])
    return jinja2.Template(open('storage/templates/base.html', 'r',encoding="utf-8").read()).render(title=serverconf['stuoe_name'],nav=nav,body=body,colorPrimary=serverconf['colorPrimary'],colorText=serverconf['colorText'],per='admin')

def gethome(auth=True,nickname='Nickname'):
    return getTemplates(auth=auth,nickname=nickname)

def  getMSG(msg):
    return getTemplates('<h4>' + msg + '</h4>')
