import typer
from rich import print
app = typer.Typer()


@app.command()
def download(url: str):
    if type(url) == str:
        print(url)

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
