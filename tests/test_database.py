from praktikum.database import Database


class TestDatabase:

    def test_init_get_buns_list_is_not_empty(self):
        database = Database()
        expected_result = 3

        assert len(database.buns) != [] and len(database.buns) == expected_result

    def test_init_get_ingredients_list_is_not_empty(self):
        database = Database()
        expected_result = 6

        assert len(database.ingredients) != [] and len(database.ingredients) == expected_result

    def test_available_buns_get_available_buns_list_is_not_empty(self):
        database = Database()
        expected_result = 3

        assert len(database.available_buns()) == expected_result

    def test_available_ingredients_get_ingredients_list_is_not_empty(self):
        database = Database()
        expected_result = 6

        assert len(database.available_ingredients()) == expected_result
