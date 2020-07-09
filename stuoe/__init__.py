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


click.echo('Welcome to Stuoe v0.1.1')
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
        os.makedirs(startworkpath + name)
        click.echo('创建目录  ' + startworkpath + name)
    if not os.listdir(startworkpath + name) == []:
        click.echo('目录为' + startworkpath + name + '的文件夹并不为空，无法创建新的工程')
        exit()
    click.echo(' Creating Project: ' + name + '  ....')
    copy_Templates_to_newproject(pastpath=startworkpath + name + '/')
    click.echo(' 项目已经成功创建 ')
    exit()


def copy_Templates_to_newproject(copypath=os.getcwd(), pastpath=os.getcwd() + '/paster/'):
    for i in os.listdir(copypath):
        if not i == '__init__.py':
            if os.path.isdir(copypath + '/' + i):
                os.makedirs(pastpath + '/' + i)
                copy_Templates_to_newproject(
                    copypath=copypath + '/'+i, pastpath=pastpath + '/' + i)
            else:
                copyfileData = open(copypath + '/' + i, 'rb').read()
                open(pastpath + '/' + i, 'wb+').write(copyfileData)
                click.echo('copying  ' + copypath + '/' +
                           i + ' -> ' + pastpath + '/' + i)


cli.add_command(run)
cli.add_command(startproject)
