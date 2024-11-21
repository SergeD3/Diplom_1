import data
from praktikum.burger import Burger


class TestBurger:

    def test_set_buns_bun_is_not_none(self, bun_mock):
        burger = Burger()
        burger.set_buns(bun_mock)

        assert burger.bun is not None and burger.bun == bun_mock

    def test_add_ingredient_add_one_ingredient_one_ingredient_added(self, ingredients_mock):
        burger = Burger()
        expected_result = 1
        burger.add_ingredient(ingredients_mock)

        assert len(burger.ingredients) == expected_result

    def test_remove_ingredient_added_one_ingredient_one_removed(self, ingredients_mock):
        burger = Burger()
        expected_result = 0

        burger.add_ingredient(ingredients_mock)
        burger.remove_ingredient(expected_result)

        assert len(burger.ingredients) == expected_result

    def test_move_ingredient_two_ingredients_swap_ingredients(self, few_ingredients_mock):
        burger = Burger()
        old_index = 1
        new_index = 0
        ingredient_one, ingredient_two = few_ingredients_mock

        burger.add_ingredient(ingredient_one)
        burger.add_ingredient(ingredient_two)
        burger.move_ingredient(index=old_index, new_index=new_index)

        assert burger.ingredients[0] == ingredient_two

    def test_get_price_get_price(self, bun_mock, ingredients_mock):
        burger = Burger()
        expected_result = bun_mock.get_price() * 2 + ingredients_mock.get_price()

        burger.set_buns(bun_mock)
        burger.add_ingredient(ingredients_mock)

        assert burger.get_price() == expected_result

    def test_get_receipt_get_receipt(self, bun_mock, ingredients_mock):
        burger = Burger()

        burger.set_buns(bun_mock)
        burger.add_ingredient(ingredients_mock)
        burger_receipt = burger.get_receipt()

        assert burger_receipt == data.RECEIPT_TEMPLATE
