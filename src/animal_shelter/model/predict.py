import logging
from pathlib import Path

import joblib
import pandas as pd
from sklearn.pipeline import Pipeline

from animal_shelter.data import load_data
from animal_shelter.features import add_features

def predict(data: Path, model_path: Path) -> pd.DataFrame:
    """
    Generate predictions on the provided data.
    :data: path to the data
    :model_path: which model to use
    """
    logger = logging.getLogger(__name__)

    raw_data = load_data(data)
    with_features = add_features(raw_data)

    categorical_features = [
        "animal_type",
        "is_dog",
        "has_name",
        "sex",
        "hair_type",
    ]
    numeric_features = ["days_upon_outcome"]

    X = with_features[categorical_features + numeric_features]
    logger.debug("Using model %s", model_path)
    model = _load_model(model_path)

    logger.info("Generating predictions")

    y_pred = model.predict_proba(X)

    # Combine predictions with class names and animal name.
    classes = model.classes_.tolist()
    proba_df = pd.DataFrame(y_pred, columns=classes).rename(str.lower, axis=1)

    predictions = raw_data[["name"]].join(proba_df)

    return predictions

def _load_model(model_path: Path) -> Pipeline:
    """
    Load the model from the given path
    :param model_path: path to the model
    :return: model pipeline
    """
    # This function could point to an experiment tracking system instead of to a local serialized model
    return joblib.load(model_path)


