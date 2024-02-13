import pytest

from sklearn.utils.validation import check_is_fitted
from sklearn.exceptions import NotFittedError
from animal_shelter.model.train import build_pipeline

@pytest.fixture()
def pipeline():
    categorical_features = [
        "animal_type",
        "is_dog",
        "has_name",
        "sex",
        "hair_type",
    ]
    numeric_features = ["days_upon_outcome"]
    return build_pipeline(categorical_features, numeric_features)


def test_pipeline(pipeline):
    assert len(pipeline.steps) == 2
    with pytest.raises(NotFittedError):
        check_is_fitted(pipeline)
