import click
from processor import Processor


@click.group()
def cli():
    click.clear()
    click.echo('[============INFRA-CLI============]')


@cli.command()
def lista_instancias():
    processor = Processor()
    click.echo(click.style('LISTANDO INSTANCIAS', fg='green'))
    click.echo(processor.lista_instancias())
