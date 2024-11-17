from praktikum.burger import Burger
from praktikum.ingredient import Ingredient


class TestBurger:

    burger = Burger()
    ingredient = Ingredient(ingredient_type='соус', name='песто', price=5.0)

    def test_set_buns_bun_not_none(self):
        self.burger.set_buns(self.burger)

        assert self.burger.bun is not None

    def test_add_ingredient_add_one_ingredient_one_ingredient_added(self):
        expected_result = 1
        self.burger.add_ingredient(self.ingredient)

        assert len(self.burger.ingredients) == expected_result

    def test_remove_ingredient_added_two_ingredients_one_removed(self):
        num = 0
        expected_result = 1

        self.burger.add_ingredient(self.ingredient)
        self.burger.add_ingredient(self.ingredient)
        self.burger.remove_ingredient(num)

        assert len(self.burger.ingredients) == expected_result

    def test_move_ingredient_two_ingredients(self):
        pass
