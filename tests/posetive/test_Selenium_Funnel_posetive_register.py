import time
from confdriver.conftest import driver
from pages.posetive.positive_register_page import Positive_Register_Page


def test_positive_scenario_register(driver):

     register_page = Positive_Register_Page(driver)
     register_page.click_on_button_register()
     register_page.send_data_in_input_username_register()
     register_page.send_data_in_input_password_register()
     register_page.click_on_button_after_fill_register()
     time.sleep(25)
     print("✅ تست مثبت با موفقیت انجام شد.")



