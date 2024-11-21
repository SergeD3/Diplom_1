from data import BUN_NAMES, BUN_PRICES
from praktikum.bun import Bun

import pytest


class TestBun:

    bun = Bun(name='', price=0.0)

    @pytest.mark.parametrize('name', BUN_NAMES)
    def test_init_set_bun_name_bun_named(self, name):
        bun_name = name
        self.bun.name = bun_name

        assert self.bun.name == bun_name

    @pytest.mark.parametrize('price', BUN_PRICES)
    def test_init_set_bun_price_bun_has_price(self, price):
        bun_price = price
        self.bun.price = bun_price

        assert self.bun.price == price

    @pytest.mark.parametrize('name', BUN_NAMES)
    def test_get_name_get_bun_name(self, name):
        bun_name = name
        self.bun.name = bun_name

        assert self.bun.get_name() == bun_name

    @pytest.mark.parametrize('price', BUN_PRICES)
    def test_get_price_get_price(self, price):
        bun_price = price
        self.bun.price = bun_price

        assert self.bun.get_price() == bun_price
