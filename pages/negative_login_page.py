from selenium.webdriver.common.by import By
from base_action.base_action import BaseActionLocator

class negative_login_page(BaseActionLocator):
    def __init__(self, driver):
        """سازنده کلاس که WebDriver را دریافت و مقداردهی می‌کند"""
        super().__init__(driver)  # فراخوانی سازنده‌ی کلاس پدر

    def click_on_Button_Vorod(self):
        self.click((By.XPATH, "//span[contains(.,'ورود')]"))

    def send_data_in_input_username_with_9_number(self):
        self.send_keys((By.ID, 'username'), '091046524')

    def send_data_in_input_username_with_char_english_in_first_numumber(self):
        self.send_keys((By.ID, 'username'), 'abc05912215')

    def send_data_in_input_password(self):
        self.send_keys((By.ID, 'password'), 'A123456789')


    def click_on_button_vorod_after_fill(self):
        self.click((By.CSS_SELECTOR, ".ps-4"))
