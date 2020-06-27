# Stuoe Start or Installing

from flask import *
from flask_sqlalchemy import SQLAlchemy
import view
import flask_mail
import flask_oauthlib
import os
import time
import jinja2
import hashlib
import re
import random
import threading

# Global Var
verify_registered_email = list()
online_user = list()
avater = open

# Get Configs File
serverconf = dict(eval(open('server.conf', 'rb').read()))
serverurl = serverconf['url']

# Init Flask
app = Flask(__name__,static_url_path='/static/',static_folder='public')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///stuoe.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.config['MAIL_SERVER'] = serverconf['stuoe_smtp_host']
app.config['MAIL_PORT'] = int(serverconf['stuoe_smtp_port'])
app.config['MAIL_USERNAME'] = serverconf['stuoe_smtp_email']
app.config['MAIL_PASSWORD'] = serverconf['stuoe_smtp_password']
app.config['MAIL_USE_SSL'] = True
app.config['SECRET_KEY'] = os.urandom(20)

# Init View
Viewrender = view


# Init DatabaseTable , Email , function
db = SQLAlchemy(app)
mail = flask_mail.Mail(app)


class User(db.Model):
    __tablename__ = 'User'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(50))
    verify_email = db.Column(db.Boolean, server_default='False')
    passhash = db.Column(db.String(50))
    nickname = db.Column(db.String(50))
    user_des = db.Column(db.String(50), server_default='该用户还什么都没写呢')
    user_session = db.Column(db.String(50), server_default='None')
    point = db.Column(db.Integer, server_default='1')
    url = db.Column(db.String(50), server_default='not url')
    user_group = db.Column(db.Integer, db.ForeignKey("Group.Group_name"))
    user_ban = db.Column(db.Boolean, server_default='False')
    user_dirty = db.Column(db.Boolean, server_default='False')
    registertime = db.Column(db.String(50))

    def __repr__(self):
        return {'id': self.id, 'email': self.email, 'user_des': self.user_des}


class Group(db.Model):
    # Waiting....
    __tablename__ = 'Group'
    Group_name = db.Column(db.String(30), primary_key=True)
    Group_des = db.Column(db.String(30), server_default='此分组还没有描述')
    Highest_authority_group = db.Column(db.Boolean, server_default='False')

    def __repr__(self):
        return self.Group_name


class Discussion(db.Model):
    # Waiting...
    __tablename__ = 'Discussion'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Discussion_title = db.Column(db.String(30))
    Discussion_body_text = db.Column(db.String(60000))
    Discussion_Publisher = db.Column(db.Integer, db.ForeignKey("User.id"))
    Discussion_watch_user = db.Column(db.Integer, db.ForeignKey("User.id"))
    Discussion_star_user = db.Column(db.Integer, db.ForeignKey("User.id"))
    Discussion_Private_in_Publisher = db.Column(
        db.Boolean, server_default='False')
    Discussion_Private_in_group = db.Column(db.Boolean, server_default='False')
    Discussion_Private_in_bbs = db.Column(db.Boolean, server_default='False')
    Discussion_No_discussion = db.Column(db.Boolean, server_default='False')
    Discussion_lock_up = db.Column(db.Boolean, server_default='False')
    Discussion_high_quality = db.Column(db.Boolean, server_default='False')
    Discussion_some_son = db.Column(db.String(40), server_default='False')


class Discussion_son(db.Model):
    # Waiting...
    __tablename__ = 'Discussion_son'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Discussion_son_Publisher = db.Column(db.Integer, db.ForeignKey("User.id"))
    Discussion_son_body_text = db.Column(db.String(60000))


db.create_all()

# Check whether two groups are created

if Group.query.filter_by(Group_name='注册用户').first() == None:
    RegisterGourp = Group(
        Group_name='注册用户', Group_des="普通的注册用户", Highest_authority_group=False)
    db.session.add(RegisterGourp)
    db.session.commit()
if Group.query.filter_by(Group_name='管理员').first() == None:
    AdminGourp = Group(
        Group_name='管理员', Group_des="维持论坛秩序，论坛所有者或者所有者的协助者", Highest_authority_group=True)
    db.session.add(AdminGourp)
    db.session.commit()

# function

def db_getuserByemail(email):
    return User.query.filter_by(email=email).first()

def db_getuserByid(id):
    return User.query.filter_by(id=id).first()


def db_check_repeat_email(email):
    if User.query.filter_by(email=email).first() == None:
        return True
    else:
        return False

def db_create_user(email, password, nickname,user_group):
    if not db_check_repeat_email(email):
        return False
    new_user = User(email=email, verify_email=False, passhash=hashlib.sha256(password.encode('utf-8')).hexdigest(), nickname=nickname, user_des='该用户还什么都没写呢',user_session='', point='1', url='', user_group=user_group, user_ban=False, user_dirty=False, registertime=str(time.time()))
    db.session.add(new_user)
    db.session.flush()
    db.session.commit()
    db_set_user_session(new_user.id)


def db_set_user_session(id):
    obj = db_getuserByid(id)
    if not obj == None:
        session_random = hashlib.sha256(str(random.randint(0,300000)).encode('utf-8')).hexdigest()
        obj.user_session = session_random
        session['id'] = id
        session['key'] = session_random
        db.session.flush()
        db.session.commit()
        return session_random
    return False






    



# Install


@app.route('/install')
def send_redict():
    if serverconf['init']:
        return abort(403)
    a = open('storage/templates/install/index.html',
             'r', encoding='utf-8').read()
    m = jinja2.Template(str(a))
    return m.render(name=serverconf['stuoe_name'], smtp_host=serverconf['stuoe_smtp_host'], smtp_port=serverconf['stuoe_smtp_port'], smtp_email=serverconf['stuoe_smtp_email'], smtp_password=serverconf['stuoe_smtp_password'], admin_mail=serverconf['stuoe_admin_mail'], admin_password=serverconf['stuoe_admin_password'])


@app.route('/install/start', methods=['GET', 'POST'])
def installing_step():
    if serverconf['init']:
        return abort(403)
    if request.method == "POST":
        print(request.form)
        stuoe_name = request.form['stuoe_name']
        stuoe_smtp_host = request.form['stuoe_smtp_host']
        stuoe_smtp_port = request.form['stuoe_smtp_port']
        stuoe_smtp_email = request.form['stuoe_smtp_email']
        stuoe_smtp_password = request.form['stuoe_smtp_password']
        stuoe_admin_mail = request.form['stuoe_admin_mail']
        stuoe_admin_password = request.form['stuoe_admin_password']
        if stuoe_name == '':
            return open('storage\stuoe\public\install_error.html', 'rb').read()
        serverconf['stuoe_name'] = stuoe_name
        serverconf['stuoe_des'] = stuoe_name
        serverconf['stuoe_smtp_host'] = stuoe_smtp_host
        serverconf['stuoe_smtp_port'] = stuoe_smtp_port
        serverconf['stuoe_smtp_email'] = stuoe_smtp_email
        serverconf['stuoe_smtp_password'] = stuoe_smtp_password
        serverconf['stuoe_admin_mail'] = stuoe_admin_mail
        serverconf['stuoe_admin_password'] = stuoe_admin_password
        serverconf['init'] = True

        db_create_user(stuoe_admin_mail,stuoe_admin_password,'Admin','管理员')
        open('server.conf', 'wb+').write(str(serverconf).encode('utf-8'))
        return redirect('/')
    else:
        return redirect('/install')

# Router
@app.route('/')
def send_index():
    return Viewrender.gethome()

# Staticfile

# None  Other StaticFile


@app.route('/stuoe.css')
def send_css():
    return open('storage/static/stuoe/stuoe.css', 'rb').read()

# API interface area


@app.route('/api/configs', methods=['GET'])
def send_api_configs():
    serverconf = dict(eval(open('server.conf', 'rb').read()))
    return str({
        'stuoe_name': serverconf['stuoe_name'],
        'stuoe_des': serverconf['stuoe_des'],
        'stuoe_themo_color': serverconf['stuoe_themo_color']
    })


@app.route('/api/register', methods=['POST'])
def send_api_register():
    request.form['nickname']
    request.form['email']
    request.form['password']
    if not re.match("^.+\\@(\\[?)[a-zA-Z0-9\\-\\.]+\\.([a-zA-Z]{2,3}|[0-9]{1,3})(\\]?)$", request.form['email']) != None:
        return Viewrender.getMSG('请填写完整的信息')
    if request.form['email'] == '':
        return Viewrender.getMSG('请填写完整的信息')
    if request.form['password'] == '':
        return Viewrender.getMSG('请填写完整的信息')
    if not User.query.filter_by(email=request.form['email']).first() == None:
        return Viewrender.getMSG('此邮箱已被注册')
    db_create_user(email=request.form['email'],password=request.form['password'],nickname=request.form['nickname'],user_group='普通用户')
    return redirect('/')




def send_mail(msg):
    with app.app_context():
        threading._start_new_thread(mail.send, (msg,))


app.run(host='0.0.0.0', port=31, debug=True)


'''
                                 Apache License
                           Version 2.0, January 2004
                        http://www.apache.org/licenses/

   TERMS AND CONDITIONS FOR USE, REPRODUCTION, AND DISTRIBUTION

   1. Definitions.

      "License" shall mean the terms and conditions for use, reproduction,
      and distribution as defined by Sections 1 through 9 of this document.

      "Licensor" shall mean the copyright owner or entity authorized by
      the copyright owner that is granting the License.

      "Legal Entity" shall mean the union of the acting entity and all
      other entities that control, are controlled by, or are under common
      control with that entity. For the purposes of this definition,
      "control" means (i) the power, direct or indirect, to cause the
      direction or management of such entity, whether by contract or
      otherwise, or (ii) ownership of fifty percent (50%) or more of the
      outstanding shares, or (iii) beneficial ownership of such entity.

      "You" (or "Your") shall mean an individual or Legal Entity
      exercising permissions granted by this License.

      "Source" form shall mean the preferred form for making modifications,
      including but not limited to software source code, documentation
      source, and configuration files.

      "Object" form shall mean any form resulting from mechanical
      transformation or translation of a Source form, including but
      not limited to compiled object code, generated documentation,
      and conversions to other media types.

      "Work" shall mean the work of authorship, whether in Source or
      Object form, made available under the License, as indicated by a
      copyright notice that is included in or attached to the work
      (an example is provided in the Appendix below).

      "Derivative Works" shall mean any work, whether in Source or Object
      form, that is based on (or derived from) the Work and for which the
      editorial revisions, annotations, elaborations, or other modifications
      represent, as a whole, an original work of authorship. For the purposes
      of this License, Derivative Works shall not include works that remain
      separable from, or merely link (or bind by name) to the interfaces of,
      the Work and Derivative Works thereof.

      "Contribution" shall mean any work of authorship, including
      the original version of the Work and any modifications or additions
      to that Work or Derivative Works thereof, that is intentionally
      submitted to Licensor for inclusion in the Work by the copyright owner
      or by an individual or Legal Entity authorized to submit on behalf of
      the copyright owner. For the purposes of this definition, "submitted"
      means any form of electronic, verbal, or written communication sent
      to the Licensor or its representatives, including but not limited to
      communication on electronic mailing lists, source code control systems,
      and issue tracking systems that are managed by, or on behalf of, the
      Licensor for the purpose of discussing and improving the Work, but
      excluding communication that is conspicuously marked or otherwise
      designated in writing by the copyright owner as "Not a Contribution."

      "Contributor" shall mean Licensor and any individual or Legal Entity
      on behalf of whom a Contribution has been received by Licensor and
      subsequently incorporated within the Work.

   2. Grant of Copyright License. Subject to the terms and conditions of
      this License, each Contributor hereby grants to You a perpetual,
      worldwide, non-exclusive, no-charge, royalty-free, irrevocable
      copyright license to reproduce, prepare Derivative Works of,
      publicly display, publicly perform, sublicense, and distribute the
      Work and such Derivative Works in Source or Object form.

   3. Grant of Patent License. Subject to the terms and conditions of
      this License, each Contributor hereby grants to You a perpetual,
      worldwide, non-exclusive, no-charge, royalty-free, irrevocable
      (except as stated in this section) patent license to make, have made,
      use, offer to sell, sell, import, and otherwise transfer the Work,
      where such license applies only to those patent claims licensable
      by such Contributor that are necessarily infringed by their
      Contribution(s) alone or by combination of their Contribution(s)
      with the Work to which such Contribution(s) was submitted. If You
      institute patent litigation against any entity (including a
      cross-claim or counterclaim in a lawsuit) alleging that the Work
      or a Contribution incorporated within the Work constitutes direct
      or contributory patent infringement, then any patent licenses
      granted to You under this License for that Work shall terminate
      as of the date such litigation is filed.

   4. Redistribution. You may reproduce and distribute copies of the
      Work or Derivative Works thereof in any medium, with or without
      modifications, and in Source or Object form, provided that You
      meet the following conditions:

      (a) You must give any other recipients of the Work or
          Derivative Works a copy of this License; and

      (b) You must cause any modified files to carry prominent notices
          stating that You changed the files; and

      (c) You must retain, in the Source form of any Derivative Works
          that You distribute, all copyright, patent, trademark, and
          attribution notices from the Source form of the Work,
          excluding those notices that do not pertain to any part of
          the Derivative Works; and

      (d) If the Work includes a "NOTICE" text file as part of its
          distribution, then any Derivative Works that You distribute must
          include a readable copy of the attribution notices contained
          within such NOTICE file, excluding those notices that do not
          pertain to any part of the Derivative Works, in at least one
          of the following places: within a NOTICE text file distributed
          as part of the Derivative Works; within the Source form or
          documentation, if provided along with the Derivative Works; or,
          within a display generated by the Derivative Works, if and
          wherever such third-party notices normally appear. The contents
          of the NOTICE file are for informational purposes only and
          do not modify the License. You may add Your own attribution
          notices within Derivative Works that You distribute, alongside
          or as an addendum to the NOTICE text from the Work, provided
          that such additional attribution notices cannot be construed
          as modifying the License.

      You may add Your own copyright statement to Your modifications and
      may provide additional or different license terms and conditions
      for use, reproduction, or distribution of Your modifications, or
      for any such Derivative Works as a whole, provided Your use,
      reproduction, and distribution of the Work otherwise complies with
      the conditions stated in this License.

   5. Submission of Contributions. Unless You explicitly state otherwise,
      any Contribution intentionally submitted for inclusion in the Work
      by You to the Licensor shall be under the terms and conditions of
      this License, without any additional terms or conditions.
      Notwithstanding the above, nothing herein shall supersede or modify
      the terms of any separate license agreement you may have executed
      with Licensor regarding such Contributions.

   6. Trademarks. This License does not grant permission to use the trade
      names, trademarks, service marks, or product names of the Licensor,
      except as required for reasonable and customary use in describing the
      origin of the Work and reproducing the content of the NOTICE file.

   7. Disclaimer of Warranty. Unless required by applicable law or
      agreed to in writing, Licensor provides the Work (and each
      Contributor provides its Contributions) on an "AS IS" BASIS,
      WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
      implied, including, without limitation, any warranties or conditions
      of TITLE, NON-INFRINGEMENT, MERCHANTABILITY, or FITNESS FOR A
      PARTICULAR PURPOSE. You are solely responsible for determining the
      appropriateness of using or redistributing the Work and assume any
      risks associated with Your exercise of permissions under this License.

   8. Limitation of Liability. In no event and under no legal theory,
      whether in tort (including negligence), contract, or otherwise,
      unless required by applicable law (such as deliberate and grossly
      negligent acts) or agreed to in writing, shall any Contributor be
      liable to You for damages, including any direct, indirect, special,
      incidental, or consequential damages of any character arising as a
      result of this License or out of the use or inability to use the
      Work (including but not limited to damages for loss of goodwill,
      work stoppage, computer failure or malfunction, or any and all
      other commercial damages or losses), even if such Contributor
      has been advised of the possibility of such damages.

   9. Accepting Warranty or Additional Liability. While redistributing
      the Work or Derivative Works thereof, You may choose to offer,
      and charge a fee for, acceptance of support, warranty, indemnity,
      or other liability obligations and/or rights consistent with this
      License. However, in accepting such obligations, You may act only
      on Your own behalf and on Your sole responsibility, not on behalf
      of any other Contributor, and only if You agree to indemnify,
      defend, and hold each Contributor harmless for any liability
      incurred by, or claims asserted against, such Contributor by reason
      of your accepting any such warranty or additional liability.

   END OF TERMS AND CONDITIONS

   APPENDIX: How to apply the Apache License to your work.

      To apply the Apache License to your work, attach the following
      boilerplate notice, with the fields enclosed by brackets "[]"
      replaced with your own identifying information. (Don't include
      the brackets!)  The text should be enclosed in the appropriate
      comment syntax for the file format. We also recommend that a
      file or class name and description of purpose be included on the
      same "printed page" as the copyright notice for easier
      identification within third-party archives.

   Copyright [yyyy] [name of copyright owner]

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
'''
