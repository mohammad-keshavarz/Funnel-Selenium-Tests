import time

from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from base_action.base_action import BaseActionLocator
from confdriver.conftest import driver


class Positive_register_page(BaseActionLocator):
    def __init__(self, driver):
        """سازنده کلاس که WebDriver را دریافت و مقداردهی می‌کند"""
        super().__init__(driver)  # فراخوانی سازنده‌ی کلاس پدر

    def click_on_button_register(self):
        self.click((By.XPATH, "//span[contains(.,'ثبت‌نام')]"))

    def send_data_in_input_username_register_click(self):
        self.click((By.CSS_SELECTOR, "[placeholder='09xxxxxxxx']"))

    def send_data_in_input_username_register(self):
        mobile_field = self.driver.find_element(By.CSS_SELECTOR, "input[placeholder='09xxxxxxxx']")
        # ارسال مقدار تستی به فیلد موبایل
        mobile_field.send_keys("09123456789")

    def send_data_in_input_password_register(self):
        self.send_keys((By.CSS_SELECTOR, "[placeholder='تعیین رمز عبور']"), 'A123456789')

    def click_on_button_register_after_fill(self):
        self.click((By.CSS_SELECTOR, ".ps-4"))
