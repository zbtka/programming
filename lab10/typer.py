import typer
from moduls import dec_zam, gen, rec
app = typer.Typer()

@app.command()
def gen1(seq: str):
    args = eval(seq)
    for combo in gen.generate_combinations(*args):
        print(combo)

@app.command()
def rec(a: str):
    print(a)


if __name__ == "__main__":
    app()
