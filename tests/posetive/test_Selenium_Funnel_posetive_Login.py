import time
from pages.posetive.positive_login_page import Positive_login_page
from confdriver.conftest import driver


def test_positive_scenario_login(driver):

    login_page = Positive_login_page(driver)
    login_page.click_on_button_vorod_posetive_login()
    login_page.send_data_in_input_username_posetive_login()
    login_page.send_data_in_input_password_posetive_login()
    login_page.click_on_button_vorod_after_fill_posetive_login()
    time.sleep(25)
    print("✅ تست مثبت با موفقیت انجام شد.")



