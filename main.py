import typer
app = typer.Typer()


@app.command()
def download(url: str):
    if type(url) == str:
        print(url)

@app.command()
def upload(url: str, globalpath: int):
    print('no')

if __name__ == '__main__':
    app()
