import typer

app = typer.Typer()

@app.command()
def delete():
    print('deleted')