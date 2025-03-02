from selenium.webdriver.common.by import By

from base_action.base_action import BaseActionLocator


class PositiveRegisterPage(BaseActionLocator):
    def __init__(self, driver):
        """سازنده کلاس که WebDriver را دریافت و مقداردهی می‌کند"""
        super().__init__(driver)  # فراخوانی سازنده‌ی کلاس والد

    def click_on_button_register(self):
        """کلیک روی دکمه ثبت‌نام"""
        self.click((By.XPATH, "//span[contains(.,'ثبت‌نام')]"))

    def send_data_in_input_username_register(self):
        """ارسال شماره موبایل در فیلد نام کاربری"""
        self.send_keys((By.ID, "input-3321073"), "09104652470")

    def send_data_in_input_password_register(self):
        """ارسال رمز عبور"""
        self.send_keys((By.CSS_SELECTOR, "[placeholder='تعیین رمز عبور']"), "root..root007")

    def click_on_button_register_after_fill(self):
        """کلیک روی دکمه ثبت‌نام پس از پر کردن فیلدها"""
        self.click((By.CSS_SELECTOR, ".ps-4"))

