import typer
import time
from rich import print
from rich.panel import Panel
from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt
from rich.markdown import Markdown
from rich.progress import track

from typing import Optional, List
import random

import mutations

# from firebaseConf import createNewUser
from firebaseConf.firebaseApp import createNewUser

MARKDOWN = """
# This is an h1

Rich can do a pretty *decent* job of rendering markdown.

1. This is a list item
2. This is another list item
"""
md = Markdown(MARKDOWN)

app = typer.Typer()
app.add_typer(mutations.app, name='mutations')
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

def _callback(value: str):
    if value != "error":
        raise typer.BadParameter("Only error is allowed")
    return value

def progress():
    total = 0
    for value in track(range(100), description="Processing..."):
        # Fake processing time
        time.sleep(0.01)
        total += 1
    print(f"Processed {total} things.")

def complete_commands():
    return ["init", "delete", "detected"]

@app.command()
def init(mutations:str = typer.Option(
        "navigation", help="The name to say hi to.", autocompletion=complete_commands
    )):
    print(mutations)

@app.command()
def createuser(command: str = typer.Option(
    ..., '--create', '-c'
)):
    if command == 'create':
        createNewUser()
    else:
        print('what yuo do?')



@app.command()
def download(
        url: Optional[str] = typer.Argument(...),
        name: str = typer.Argument(..., help="The name of the user to greet", autocompletion=complete_commands),
        password: str = typer.Option(
            ..., prompt=True, confirmation_prompt=True, hide_input=True
        ),
        user_name: str = typer.Option(..., "--name", '-n'), # Here option cli with -n reading so --name
        formal: str = typer.Option(False, "--formal", '-f'), # Here option cli with -f reading so --formal
        random_int: Optional[int] = typer.Argument(random.choice([0,1,2,3,4,5,6])),
        ):
        # python main.py download 'quest' eric --name Browse - It's so request to console. Need to past this in powershell or cmd
    if url == 'quest':
        progress()
        print(random_int)
        print(name)
        print(user_name)
        print(formal)
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
