import pandas as pd
from pandas.testing import assert_series_equal

import pytest

from animal_shelter.features import (
    check_has_name,
    get_sex,
    get_hair_type,
    get_neutered,
    compute_days_upon_outcome,
)


def test_check_has_name():
    s = pd.Series(["Ivo", "Henk", "unknown"])
    result = check_has_name(s)
    expected = pd.Series([True, True, False])
    assert_series_equal(result, expected)


@pytest.fixture(scope="module")
def sex():
    return pd.Series(
        [
            "Neutered Male",
            "Spayed Female",
            "Intact Male",
            "Intact Female",
            "Unknown",
            "whale",
        ]
    )


def test_get_sex(sex):
    result = get_sex(sex)
    expected = pd.Series(["male", "female", "male", "female", "unknown", "unknown"])
    assert_series_equal(result, expected)


def test_get_neutered(sex):
    result = get_neutered(sex)
    expected = pd.Series(["fixed", "fixed", "intact", "intact", "unknown", "unknown"])
    assert_series_equal(result, expected)


def test_get_hair_type():
    s = pd.Series(
        [
            "Shetland Sheepdog Mix",
            "Pit Bull Mix",
            "Cairn Terrier/Chihuahua Shorthair",
            "Domestic Medium Hair Mix",
            "Chihuahua Longhair Mix",
        ]
    )
    result = get_hair_type(s)
    expected = pd.Series(["unknown", "unknown", "shorthair", "medium hair", "longhair"])
    assert_series_equal(result, expected)


def test_compute_days_upon_outcome():
    s = pd.Series(
        [
            "1 year",
            "2 years",
            "1 month",
            "2 months",
            "1 weeks",
            "2 week",
            "1 days",
            "2 day",
        ]
    )
    result = compute_days_upon_outcome(s)
    expected = pd.Series([365.0, 2 * 365.0, 30.0, 2 * 30.0, 7.0, 14.0, 1.0, 2.0])
    assert_series_equal(result, expected)
