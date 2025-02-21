from selenium.webdriver.common.by import By
from base_action.base_action import BaseActionLocator

class Positive_login_page(BaseActionLocator):
    def __init__(self, driver):
        """سازنده کلاس که WebDriver را دریافت و مقداردهی می‌کند"""
        super().__init__(driver)  # فراخوانی سازنده‌ی کلاس پدر

    def click_on_Button_Vorod(self):
        self.click((By.XPATH, "//span[contains(.,'ورود')]"))

    def send_data_in_input_username(self):
        self.send_keys((By.ID, 'username'), '09104652470')

    def send_data_in_input_password(self):
        self.send_keys((By.ID, 'password'), 'A123456789')

    def click_on_button_vorod_after_fill(self):
        self.click((By.CSS_SELECTOR, ".ps-4"))
