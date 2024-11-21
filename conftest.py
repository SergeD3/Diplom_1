import pytest

from unittest.mock import Mock
import data


@pytest.fixture
def bun_mock():
    bun_mock = Mock()
    bun_mock.get_name.return_value = data.MOCK_BUN_NAME
    bun_mock.get_price.return_value = data.MOCK_BUN_PRICE

    return bun_mock


@pytest.fixture
def ingredients_mock():
    ing_mock = Mock()
    ing_mock.get_name.return_value = data.MOCK_ING_NAME_1
    ing_mock.get_price.return_value = data.MOCK_ING_PRICE_1
    ing_mock.get_type.return_value = data.MOCK_ING_TYPE_1

    return ing_mock


@pytest.fixture
def few_ingredients_mock(ingredients_mock):
    few_mock = Mock()
    few_mock.get_name.return_value = data.MOCK_ING_NAME_2
    few_mock.get_price.return_value = data.MOCK_ING_PRICE_2
    few_mock.get_type.return_value = data.MOCK_ING_TYPE_2

    return [ingredients_mock, few_ingredients_mock]
