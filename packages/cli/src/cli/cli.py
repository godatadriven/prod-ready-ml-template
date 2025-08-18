import logging
from pathlib import Path

import typer

from animal_shelter.model.predict import predict as predict_model
from animal_shelter.model.train import train as train_model

app = typer.Typer()


@app.callback()
def main() -> None:
    """Determine animal shelter outcomes."""
    logging.basicConfig(
        level=logging.DEBUG,
        format="[%(asctime)-15s] %(name)s - %(levelname)s - %(message)s",
    )


@app.command()
def train(input_path: Path, model_path: Path) -> None:
    """Trains a model on the given dataset."""
    typer.echo(f"Loading {input_path}")
    train_model(input_path, model_path)


@app.command()
def predict(input_path: Path, model_path: Path, output_path: Path) -> None:
    """Applies a model to the given dataset."""
    typer.echo(f"Loading {input_path}")
    predictions = predict_model(input_path, model_path)

    typer.echo(f"Writing predictions to {output_path}")
    predictions.to_csv(output_path, index=False, header=True)
