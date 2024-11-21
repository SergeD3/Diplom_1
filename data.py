from praktikum import ingredient_types

BUN_NAMES = [
        'q',
        'qwe'
        'great buns bro',
        'Lorem ipsum dolor sit amet consectetuer adipiscing elit sed diam nonummy nibh euismod tincidunt ut laoreet '
        'dolore magna aliquam erat volutpat',
        'а',
        'абв'
        'отличные у тебя булки брат!'
    ]

BUN_PRICES = [0, 25.7, 9999999.9, -1, -74.8, -9999999.9]

# Mock data
MOCK_BUN_NAME = 'Галактическая булка'
MOCK_BUN_PRICE = 50.0

MOCK_ING_NAME_1 = 'Кетчунез'
MOCK_ING_PRICE_1 = 50.0
MOCK_ING_TYPE_1 = ingredient_types.INGREDIENT_TYPE_SAUCE

MOCK_ING_NAME_2 = 'Котлета Красная Цена'
MOCK_ING_PRICE_2 = 100.0
MOCK_ING_TYPE_2 = ingredient_types.INGREDIENT_TYPE_FILLING

RECEIPT_TEMPLATE = (
        f'(==== Галактическая булка ====)\n'
        f'= sauce Кетчунез =\n'
        f'(==== Галактическая булка ====)\n'
        '\n'
        f'Price: 150.0'
        )
