import time
from base_action.base_action import BaseActionLocator
from pages.positive_login_page import Positive_login_page
from confdriver.conftest import driver


def test_positive_scenario(driver):


    """تست سناریوی مثبت برای باز کردن تب‌ها و انتخاب گزینه‌ها"""
    print("dirver", driver)
    # ایجاد نمونه‌ای از Positive_test
    login_page = Positive_login_page(driver)
    print("dirver", driver)

    login_page.click_on_Button_Vorod()
    login_page.send_data_in_input_username()
    login_page.send_data_in_input_password()
    login_page.click_on_button_vorod_after_fill()


    time.sleep(50)





    print("✅ تست مثبت با موفقیت انجام شد.")



