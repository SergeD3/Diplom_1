import pytest
import data


class TestIngredient:

    @pytest.mark.parametrize('ingredient', data.INGREDIENTS)
    def test_init_get_ingredient_type(self, ingredient):
        expected_result = ingredient.type

        assert ingredient.get_type() == expected_result

    @pytest.mark.parametrize('ingredient', data.INGREDIENTS)
    def test_init_get_ingredient_name(self, ingredient):
        expected_result = ingredient.name

        assert ingredient.get_name() == expected_result

    @pytest.mark.parametrize('ingredient', data.INGREDIENTS)
    def test_init_get_ingredient_price(self, ingredient):
        expected_result = ingredient.price

        assert ingredient.get_price() == expected_result
