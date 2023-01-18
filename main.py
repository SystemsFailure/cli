import typer
from rich import print
from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt

app = typer.Typer()
console = Console()

def structureDisplay(name, age):
    table = Table(f"{name}", f"{age}")
    table.add_row("Rick", "200")
    table.add_row("Morty", "18")
    console.print(table)

def defaultASK():
    name = Prompt.ask("Enter your name")
    print(name)

@app.command()
def download(url: str):
    if type(url) == str:
        print(url)
        structureDisplay()

@app.command()
def upload(url: str, globalpath: str = '', formal: bool = False):
    """
    This is documentation from lovela! :)
    """
    if formal:
        print('[bold cyan2]Access[/bold cyan2] : ' + 'succesful upload from : {}'.format(url))
    else:
        print('[bold red]Error[/bold red] : ' + 'not access. Wheare --formal? write --formal - txt')
if __name__ == '__main__':
    app()
