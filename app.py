import click

click.echo('Welcome to Stuoe v0.1.1')
click.echo('')

@click.group()
def cli():
    pass


@click.command()
@click.option("--port", default=3000, help="Runing Stuoe", type=int)
def run(port):
    click.echo('Start Runing...')
    import stuoe as app
    app.app.run(host='0.0.0.0',port=port)

cli.add_command(run)

cli()

