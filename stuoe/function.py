from master import db
from master import Viewrender
from models import *


def db_getuserByemail(email):
    return User.query.filter_by(email=email).first()


def db_getuserByid(id):
    return User.query.filter_by(id=id).first()


def db_getpostByid(id):
    return Post.query.filter_by(id=id).first()


def db_gettagsByname(name):
    return Tags.query.filter_by(name=name).first()


def db_getGroupByid(name):
    return Group.query.filter_by(name=name).first()


def db_check_repeat_email(email):
    if User.query.filter_by(email=email).first() is None:
        return True
    else:
        return False


def db_create_user(email, password, nickname, user_group):
    if not db_check_repeat_email(email):
        return False
    new_user = User(
        email=email,
        verify_email=False,
        passhash=hashlib.sha256(
            password.encode('utf-8')).hexdigest(),
        nickname=nickname,
        user_des='Wait....And Something Text About This User',
        user_session='',
        point='1',
        url='',
        user_group=user_group,
        user_ban=False,
        user_dirty=False,
        registertime=time.time(),
        MessageToMailbox=True,
        avater='http://identicon.relucks.org/' + str(random.randint(200, 999)) + '?size=120')
    db.session.add(new_user)
    db.session.flush()
    db.session.commit()
    db_set_user_session(new_user.id)


def db_set_user_session(id):
    obj = db_getuserByid(id)
    if obj is not None:
        session_random = hashlib.sha256(
            str(random.randint(0, 300000)).encode('utf-8')).hexdigest()
        obj.user_session = session_random
        session['id'] = id
        session['key'] = session_random
        db.session.flush()
        db.session.commit()
        return session_random
    return False


def get_session(type='nickname'):
    if session.get('id') is None or session.get('key') is None:
        session.clear()
        return False
    obj = db_getuserByid(session.get('id'))
    if obj is None:
        return False
    if obj.user_session == session.get('key'):
        if type == 'nickname':
            return obj.nickname
        elif type == 'id':
            return obj.id
        elif type == 'obj':
            return obj

    else:
        session.clear()


def getPost_list(tags='', num=30):
    returnPost_list = []
    if tags == '':
        for i in Post.query.filter_by().all()[:num]:
            if i.top:
                returnPost_list.insert(0, i)
            else:
                returnPost_list.append(i)
    else:
        for i in Post.query.filter_by(tags=tags).all()[:num]:
            if i.top:
                returnPost_list.insert(0, i)
            else:
                returnPost_list.append(i)
    return returnPost_list
