import click
from src.processor import Processor
from src.prettytable import clean_instances
from utils import INFRA_CLI


@click.group()
def cli():
    click.echo(INFRA_CLI)


@cli.command()
def lista_instancias():
    processor = Processor()
    click.echo(click.style('LISTANDO INSTANCIAS', fg='green'))
    click.echo(clean_instances(processor.lista_instancias()))
