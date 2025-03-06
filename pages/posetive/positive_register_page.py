from selenium.webdriver.common.by import By
from base_action.base_action import BaseActionLocator


class Positive_Register_Page(BaseActionLocator):

    def __init__(self, driver):
        super().__init__(driver)


    def click_on_button_register(self):

        self.click((By.XPATH, "//span[contains(.,'ثبت‌نام')]"))

    def send_data_in_input_username_register(self):

        self.send_keys((By.ID, "register-username"), "09104652470")

    def send_data_in_input_password_register(self):

        self.send_keys((By.ID, "register-password"), "A@123456789000")

    def click_on_button_after_fill_register(self):

        self.click((By.XPATH, "//span[@class='flex items-center justify-center gap-x-2 w-full whitespace-nowrap py-2 ps-4 pe-4']"))

