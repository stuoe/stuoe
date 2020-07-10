# -*- coding: utf-8 -*-
"""
    Stuoe
    ~~~~~

    Stuoe is a python module for beginners and developers who want to build 
    forums quickly. The interface is simple and easy to install

    :copyright: (c) 2020 by SNBCK.
    :license: Apache License, see LICENSE for more details.
    
"""


import os
import click


startworkpath = os.getcwd() + '/'

os.chdir(os.path.dirname(__file__))

__version__ = '0.1.2.4'


click.echo('Welcome to Stuoe ' + __version__) 
click.echo('Worker in ' + os.getcwd())
click.echo('')


@click.group()
def cli():
    '''
    This is the main group of the stuoe command line tools
    '''
    pass


@click.command()
@click.option("--port", default=3000, help="Runing Stuoe", type=int)
def run(port):
    click.echo('Start Runing...')
    click.echo('Worker in ' + os.getcwd())
    try:
        import app
    except:
        from stuoe import app
    app.app.run(host='0.0.0.0', port=port)


@click.command()
@click.option("--name", default='Dafault', help="Start A New Project", type=str)
def startproject(name):
    if not os.path.exists(startworkpath + name):
        click.echo('Create  ' + startworkpath + name)
    if not os.listdir(startworkpath + name) == []:
        click.echo('目录为' + startworkpath + name + '的文件夹并不为空，无法创建新的工程')
        exit()
    click.echo('Creating Project: ' + name + '  ....')
    copy_Templates_to_newproject(pastpath=startworkpath + name + '/')
    click.echo('项目已经成功创建 ')
    exit()

@click.command()
@click.option("--name", default='Dafault', help="A Update", type=str)
def update(name):
    if not os.path.exists(startworkpath + name):
        try:
            os.makedirs(startworkpath + name)
            click.echo('Create  ' + startworkpath + name)
        except:
            pass
    click.echo('Update Project: ' + name + '  ....')
    copy_Templates_to_newproject(pastpath=startworkpath + name + '/')
    click.echo('项目已经成功更新 ')
    exit()

'''
@click.command()
@click.option("--host", default='0.0.0.0', help="Runing Server Host", type=str)
@click.option("--port", default=3000, help="Runing Server Port", type=int)
@click.option("--debug", default=False, help="Runing Server Debug", type=bool)
def runserver(host,port,debug):
    if not os.path.exists(startworkpath + 'app.py'):
        click.echo('目录下没有文件app.py，无法启动项目')
    if not os.path.exists(startworkpath + 'server.conf'):
        click.echo('目录下没有文件server.conf，无法启动项目')
    os.chdir(startworkpath + '/')
    click.echo('Worker in ' + os.getcwd())
    __import__(r"app")
    app.app.run(host=host,port=port,debug=debug)

'''
def copy_Templates_to_newproject(copypath=os.getcwd(), pastpath=os.getcwd() + '/paster/'):
    for i in os.listdir(copypath):
        if not (i == '__init__.py' or i == 'server.conf' or i == 'sqlite3.db'):
            if os.path.isdir(copypath + '/' + i):
                try:
                    os.makedirs(pastpath + '/' + i)
                except:
                    pass
                copy_Templates_to_newproject(
                    copypath=copypath + '/'+i, pastpath=pastpath + '/' + i)
            else:
                copyfileData = open(copypath + '/' + i, 'rb').read()
                open(pastpath + '/' + i, 'wb+').write(copyfileData)
                click.echo('copying  ' + copypath + '/' +
                           i + ' -> ' + pastpath + '/' + i)


cli.add_command(run)
cli.add_command(startproject)
cli.add_command(update)
