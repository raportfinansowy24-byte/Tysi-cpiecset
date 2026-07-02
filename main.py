import typer

from pipeline import Pipeline


app = typer.Typer()


@app.command()
def run(
    topic: str
):

    pipe = Pipeline()

    result = pipe.run(topic)

    print()

    print(result["title"])

    print()

    print(result["voiceover"])


if __name__ == "__main__":

    app()
