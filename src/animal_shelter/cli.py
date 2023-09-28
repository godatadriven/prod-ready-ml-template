import logging
from pathlib import Path

import joblib
import pandas as pd
import typer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import GridSearchCV

from animal_shelter.data import load_data

app = typer.Typer()


@app.callback()
def main() -> None:
    """Determine animal shelter outcomes."""
    logging.basicConfig(
        level=logging.INFO,
        format="[%(asctime)-15s] %(name)s - %(levelname)s - %(message)s",
    )


@app.command()
def train(input_path: Path, model_path: Path) -> None:
    """Trains a model on the given dataset."""

    typer.echo(f"Loading {input_path}")

    logger = logging.getLogger(__name__)

    logger.info("Loading input dataset from %s", input_path)
    train_dataset = load_data(input_path)
    logger.info("Found %i rows", len(train_dataset))

    # - Separate feature matrix X from target y
    X = train_dataset.drop("outcome_type", axis=1)
    y = train_dataset["outcome_type"]

    # - add/remove features such that the feature matrix X is suitable for ML
    simple_cols = ["animal_type", "sex_upon_outcome"]
    X_train_dummies = pd.get_dummies(X.loc[:, simple_cols])

    # - Fit a model
    logger.info("Training model")
    param_grid = {"C": [1e-3, 1e-2, 1e-1]}
    grid_search = GridSearchCV(
        LogisticRegression(), param_grid=param_grid, scoring="neg_log_loss"
    )

    grid_search.fit(X_train_dummies, y)

    # - Log the final score
    logger.info(f"Best score: {grid_search.best_score_}")

    # - Save model
    best_model = grid_search.best_estimator_
    joblib.dump(best_model, model_path)

    logger.info(f"Wrote model to {model_path}")


@app.command()
def predict(input_path: Path, model_path: Path, output_path: Path) -> None:
    """Applies a model to the given dataset."""

    typer.echo(f"Loading {input_path}")

    logger = logging.getLogger(__name__)

    logger.info("Loading input dataset from %s", input_path)
    X = load_data(input_path)  # We don't have labels
    logger.info("Found %i rows", len(X))
    logger.info("Loading model from %s", model_path)

    model = joblib.load(model_path)

    logger.info("Running the model")
    simple_cols = ["animal_type", "sex_upon_outcome"]
    X_dummies = pd.get_dummies(X.loc[:, simple_cols])
    y_pred = model.predict_proba(X_dummies)

    classes = model.classes_.tolist()
    proba_df = pd.DataFrame(y_pred, columns=classes)

    logger.info(f"Writing predictions to {output_path}")
    proba_df["id"] = X["id"]
    reordered = proba_df[["id"] + classes]
    reordered.to_csv(output_path, index=False)
