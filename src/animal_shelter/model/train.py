import logging
from pathlib import Path

import joblib
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestClassifier
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

from animal_shelter.data import load_data
from animal_shelter.features import add_features


def train(data: Path, model_path: Path) -> None:
    "Train model on the provided data and save it to the `model_path`."

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
    y = with_features["outcome_type"]
    pipeline = _build_pipeline(categorical_features, numeric_features)
    logger.debug("Fitting model")
    model = _fit_model(pipeline, X, y)

    _save_model(model, model_path)


def _build_pipeline(cat_features: list, num_features: list) -> Pipeline:
    """
    Build the model pipeline
    :param cat_features: list of categorical features
    :param num_features: list of numerical features
    :return: model pipeline
    """

    num_transformer = Pipeline(
        steps=[("imputer", SimpleImputer()), ("scaler", StandardScaler())]
    )
    cat_transformer = Pipeline(steps=[("onehot", OneHotEncoder(drop="first"))])
    transformer = ColumnTransformer(
        (
            ("numeric", num_transformer, num_features),
            ("categorical", cat_transformer, cat_features),
        )
    )
    clf_model = Pipeline(
        [("transformer", transformer), ("model", RandomForestClassifier())]
    )
    return clf_model


def _fit_model(model: Pipeline, X: pd.DataFrame, y: pd.Series) -> Pipeline:
    """
    Train the model
    :param model: model pipeline
    :param X: features
    :param y: target variable
    :return: trained model pipeline
    """

    return model.fit(X, y)


def _save_model(model: Pipeline, path: Path) -> None:
    """
    Save the model.
    :param model: model object
    :param path: path to the model
    """
    logger = logging.getLogger(__name__)
    logger.info("Saving model at %s", path)
    joblib.dump(model, path)
