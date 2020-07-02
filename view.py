import jinja2


# Get Configs File
serverconf = dict(eval(open('server.conf', 'rb').read()))
serverurl = serverconf['url']

# And Base Templates



def getTemplates(body='',title=serverconf['stuoe_name'],userObj='',auth=False):
    if auth:
         nav = jinja2.Template(open('storage/templates/nav/user.html','r',encoding="utf-8").read()).render(title=title + ' - ' + serverconf['stuoe_name'],userObj=userObj,webtitle=serverconf['stuoe_name'])
    else:
         nav = jinja2.Template(open('storage/templates/nav/nouser.html','r',encoding="utf-8").read()).render(title=serverconf['stuoe_name'])
    return jinja2.Template(open('storage/templates/base.html', 'r',encoding="utf-8").read()).render(title=serverconf['stuoe_name'],nav=nav,body=body,colorPrimary=serverconf['colorPrimary'],colorText=serverconf['colorText'],per='admin',webtitle=serverconf['stuoe_name'])

def gethome(auth=True,nickname='Nickname',userObj=''):
    return getTemplates(auth=auth,title='',userObj=userObj)

def getMSG(msg,auth=False,userObj=''):
    return getTemplates('<h4>' + msg + '</h4>',title='Messages',auth=auth,userObj=userObj)

def getUserSpace(auth=False,lookuserObj='',userObj=''):
    body = jinja2.Template(open('storage/templates/user.html','r',encoding="utf-8").read()).render(userObj=lookuserObj)
    return getTemplates(body=body,auth=auth,userObj=userObj)

def getWrite(auth=False,userObj=''):
    return getTemplates(body=open('storage/templates/write.html','r',encoding="utf-8").read(),auth=auth,userObj=userObj,title='编辑帖子')
    
def getSettings(userObj=''):
    body = jinja2.Template(open('storage/templates/settings.html','r',encoding="utf-8").read()).render(UserObj=userObj)
    return getTemplates(body=body,auth=True,userObj=userObj)