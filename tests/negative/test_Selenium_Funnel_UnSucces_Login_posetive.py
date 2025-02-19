# test_negative_scenario.py
import pytest
from pages.trade_page import TradePage
from confdriver.conftest import driver


def test_negative_scenario(driver):
    print("driver test negative", driver)
    trade_page = TradePage(driver)
    with pytest.raises(Exception):
        trade_page.click(("wrong_locator_type", "wrong_locator_value"))
    print(" ✅ تست منفی با موفقیت انجام شد.")
