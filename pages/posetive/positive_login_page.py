from selenium.webdriver.common.by import By
from base_action.base_action import BaseActionLocator



class Positive_login_page(BaseActionLocator):

    def __init__(self, driver):
        super().__init__(driver)


    def click_on_button_vorod_posetive_login(self):
        self.click((By.XPATH, "//span[contains(.,'ورود')]"))

    def send_data_in_input_username_posetive_login(self):
        self.send_keys((By.ID, 'username'), '09104652470')

    def send_data_in_input_password_posetive_login(self):
        self.send_keys((By.ID, 'password'), 'root..root007')

    def click_on_button_vorod_after_fill_posetive_login(self):
        self.click((By.CSS_SELECTOR, ".ps-4"))
