import typer
from rich import print
from rich.panel import Panel
from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt
from rich.markdown import Markdown

from typing import Optional
import random

MARKDOWN = """
# This is an h1

Rich can do a pretty *decent* job of rendering markdown.

1. This is a list item
2. This is another list item
"""
md = Markdown(MARKDOWN)

app = typer.Typer()
console = Console()
err_console = Console(stderr=True)

def structureDisplay(name, age):
    table = Table(f"{name}", f"{age}")
    table.add_row("Rick", "200")
    table.add_row("Morty", "18")
    console.print(table)

def defaultASK():
    name = Prompt.ask("Enter your name", default='None')
    print(name)

@app.command()
def download(
        url: Optional[str] = typer.Argument(...),
        name: str = typer.Argument(..., help="The name of the user to greet"),
        password: str = typer.Option(
            ..., prompt=True, confirmation_prompt=True, hide_input=True
        ),
        random_int: Optional[int] = typer.Argument(random.choice([0,1,2,3,4,5,6])),
        ):
    if url == 'quest':
        print(random_int)
        print(name)
        print(password)
        console.print(md)
        print(Panel("Hello, [green]USER!", title="Welcome", subtitle="Thank you for view!"))
        structureDisplay('name', 'age')
        if url == 'abort':
            raise typer.Abort()
    elif url == 'error':
        err_console.print("[bold red]Error[/bold red] : " + "not access, you writed type int? needly in string, please, editing your quota!")
    else:
        raise typer.Exit()
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
