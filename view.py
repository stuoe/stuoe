import jinja2
import random
import time


# Get Configs File
serverconf = dict(eval(open('server.conf', 'rb').read()))
serverurl = serverconf['url']

# And Base Templates

m1 = jinja2.Template(
    '<h1>账号邮箱变动</h1><br>原先的邮箱：{{ oldemail}} 将停用，改用 {{ newemail }} 作为新的邮箱<br><code>验证码:{{ code }}')


def c():
    # Get Configs File
    serverconf = dict(eval(open('server.conf', 'rb').read()))
    serverurl = serverconf['url']


def getTemplates(
        body='',
        title='',
        userObj='',
        auth=False,
        base2=False):
    if auth:
        nav = jinja2.Template(
            open(
                'storage/templates/nav/user.html',
                'r',
                encoding="utf-8").read()).render(
            title=title,
            userObj=userObj,
            webtitle=serverconf['stuoe_name'],
            js=serverconf['js'])
    else:
        nav = jinja2.Template(
            open(
                'storage/templates/nav/nouser.html',
                'r',
                encoding="utf-8").read()).render(
            title=serverconf['stuoe_name'],
            webtitle=serverconf['stuoe_name'],
            js=serverconf['js'])
    if base2:
        return jinja2.Template(
            open(
                'storage/templates/base2.html',
                'r',
                encoding="utf-8").read()).render(
            title=serverconf['stuoe_name'],
            nav=nav,
            body=body,
            colorPrimary=serverconf['colorPrimary'],
            colorText=serverconf['colorText'],
            per='admin',
            webtitle=serverconf['stuoe_name'],
            js=serverconf['js'])
    else:
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
            webtitle=serverconf['stuoe_name'],
            js=serverconf['js'])


def gethome(auth=True, userObj='', tagslist='', postlist='', get_avater=''):
    body = jinja2.Template(open('storage/templates/index.html',
                                'r', encoding="utf-8").read()).render(webtitle=serverconf['stuoe_name'], des=serverconf['stuoe_des'], userObj=userObj, tagslist=tagslist, postlist=list(postlist), get_avater=get_avater)
    return getTemplates(auth=auth, title='', body=body, userObj=userObj, base2=True)


def getMSG(msg, auth=False, userObj=''):
    return getTemplates(
        '<h4>' + msg + '</h4>',
        title='Messages',
        auth=auth,
        userObj=userObj)


def getUserSpace(auth=False, lookuserObj='', userObj=''):
    body = jinja2.Template(open('storage/templates/user.html',
                                'r', encoding="utf-8").read()).render(userObj=lookuserObj)
    return getTemplates(
        body=body,
        auth=auth,
        userObj=userObj,
        title=lookuserObj.nickname)


def getWrite(auth=False, userObj='', Tags=''):
    body = jinja2.Template(open(
        'storage/templates/write.html',
        'r',
        encoding="utf-8").read()).render(Tags=Tags)
    return getTemplates(
        body=body,
        auth=auth,
        userObj=userObj,
        title='编辑帖子')


def getSettings(userObj=''):
    body = jinja2.Template(open('storage/templates/settings.html',
                                'r', encoding="utf-8").read()).render(UserObj=userObj)
    return getTemplates(
        body=body,
        auth=True,
        userObj=userObj,
        title=userObj.nickname)


def renderEmailCheckMessages(userObj, newemail):
    randomcode = str(random.randint(1000, 9999))
    msg = m1.render(oldemail=userObj.email, newemail=newemail, code=randomcode)
    return {'msg': msg, 'code': randomcode}


def getCheck(userObj):
    body = jinja2.Template(open('storage/templates/check.html',
                                'r', encoding="utf-8").read()).render(UserObj=userObj)
    return getTemplates(body=body, auth=True, userObj=userObj, title='验证邮箱')


def getPost(
        auth=False,
        userObj='',
        pusherUserObj='',
        Post='',
        Tags='',
        replyList=''):
    body = jinja2.Template(
        open(
            'storage/templates/post.html',
            'r',
            encoding="utf-8").read()).render(
        user=pusherUserObj,
        post=Post,
        tags=Tags,
        ReplyList=replyList,
        list=list)
    return getTemplates(
        body=body,
        auth=auth,
        userObj=userObj,
        title=Post.title)
