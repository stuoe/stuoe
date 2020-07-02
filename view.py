import jinja2
import random


# Get Configs File
serverconf = dict(eval(open('server.conf', 'rb').read()))
serverurl = serverconf['url']

# And Base Templates

m1 = jinja2.Template(
    '<h1>账号邮箱变动</h1><br>原先的邮箱：{{ oldemail}} 将停用，改用 {{ newemail }} 作为新的邮箱<br><code>验证码:{{ code }}')


def getTemplates(
        body='',
        title=serverconf['stuoe_name'],
        userObj='',
        auth=False):
    if auth:
        nav = jinja2.Template(
            open(
                'storage/templates/nav/user.html',
                'r',
                encoding="utf-8").read()).render(
            title=title +
            ' - ' +
            serverconf['stuoe_name'],
            userObj=userObj,
            webtitle=serverconf['stuoe_name'])
    else:
        nav = jinja2.Template(
            open(
                'storage/templates/nav/nouser.html',
                'r',
                encoding="utf-8").read()).render(
            title=serverconf['stuoe_name'])
    return jinja2.Template(
        open(
            'storage/templates/base.html',
            'r',
            encoding="utf-8").read()).render(
        title=serverconf['stuoe_name'],
        nav=nav,
        body=body,
        colorPrimary=serverconf['colorPrimary'],
        colorText=serverconf['colorText'],
        per='admin',
        webtitle=serverconf['stuoe_name'])


def gethome(auth=True, nickname='Nickname', userObj=''):
    return getTemplates(auth=auth, title='', userObj=userObj)


def getMSG(msg, auth=False, userObj=''):
    return getTemplates(
        '<h4>' + msg + '</h4>',
        title='Messages',
        auth=auth,
        userObj=userObj)


def getUserSpace(auth=False, lookuserObj='', userObj=''):
    body = jinja2.Template(open('storage/templates/user.html',
                                'r', encoding="utf-8").read()).render(userObj=lookuserObj)
    return getTemplates(body=body, auth=auth, userObj=userObj)


def getWrite(auth=False, userObj=''):
    return getTemplates(
        body=open(
            'storage/templates/write.html',
            'r',
            encoding="utf-8").read(),
        auth=auth,
        userObj=userObj,
        title='编辑帖子')


def getSettings(userObj=''):
    body = jinja2.Template(open('storage/templates/settings.html',
                                'r', encoding="utf-8").read()).render(UserObj=userObj)
    return getTemplates(body=body, auth=True, userObj=userObj)


def renderEmailCheckMessages(userObj, newemail):
    randomcode = str(random.randint(1000, 9999))
    msg = m1.render(oldmail=userObj.email, newemail=newemail, code=randomcode)
    return {'msg': msg, 'code': randomcode}


def getCheck(userObj):
    body = jinja2.Template(open('storage/templates/check.html',
                                'r', encoding="utf-8").read()).render(UserObj=userObj)
    return getTemplates(body=body, auth=True, userObj=userObj)
