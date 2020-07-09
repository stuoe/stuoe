import os
import click


''' 
-----------------------------
    Start CLI
-----------------------------
'''

os.chdir(os.path.dirname(__file__))



click.echo('Welcome to Stuoe v0.1.1')
click.echo('Worker in ' + os.getcwd())
click.echo('')


@click.group()
def cli():
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
def startproject(port):
    click.echo('Start Runing...')
    app.run(host='0.0.0.0', port=port)


cli.add_command(run)
cli.add_command(startproject)
