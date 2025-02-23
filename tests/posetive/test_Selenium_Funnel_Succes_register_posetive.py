import time
from base_action.base_action import BaseActionLocator
from pages.positive_register_page import Positive_register_page
from confdriver.conftest import driver


def test_positive_scenario(driver):


    """تست سناریوی مثبت برای باز کردن تب‌ها و انتخاب گزینه‌ها"""
    print("dirver", driver)
    # ایجاد نمونه‌ای از Positive_test
    register_page = Positive_register_page(driver)
    print("dirver", driver)

    register_page.click_on_button_register()
    #register_page.send_data_in_input_username_register_click()
    #register_page.send_data_in_input_username_register()
    #register_page.send_data_in_input_password_register()


    time.sleep(3)