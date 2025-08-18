# import pandas as pd
# from pandas.testing import assert_series_equal
import pytest

from animal_shelter import data


def test_convert_camel_case():
    assert data.convert_camel_case("CamelCase") == "camel_case"
    assert data.convert_camel_case("CamelCASE") == "camel_case"
    assert data.convert_camel_case("camel-case") != "camel_case"
    assert data.convert_camel_case("camel_case") == "camel_case"
    assert data.convert_camel_case("camel case") != "camel_case"
    with pytest.raises(TypeError) as exception:
        data.convert_camel_case(123)
    assert "expected string or bytes" in str(exception.value)


@pytest.fixture(scope="class")
def list_of_numbers():
    return [1, 2, 3, 4, 5]


class TestListFunctions:
    def test_all_nums(self, list_of_numbers):
        assert all(type(element) is int for element in list_of_numbers)
        # ruff might complain, but using isinstance doesn't work for this toy example
        assert not all(type(element) is int for element in [True, 3, 4])
        assert all(isinstance(element, int) for element in [True, 3, 4])

    def test_sum(self, list_of_numbers):
        assert sum(list_of_numbers) == 15
