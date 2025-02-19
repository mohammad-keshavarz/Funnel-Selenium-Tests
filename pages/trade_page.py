import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class TradePage:
    def __init__(self, driver):
        """سازنده کلاس که WebDriver را دریافت و مقداردهی می‌کند"""
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def click(self, locator):
        """کلیک روی یک عنصر با استفاده از Locator"""
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def send_keys(self, locator, value):
        """ارسال مقدار به یک عنصر با استفاده از Locator"""
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.clear()  # پاک کردن مقدار قبلی (در صورت وجود)
        element.send_keys(value)






    def click_on_Button_Vorod(self):
        self.click((By.XPATH,"//span[contains(.,'ورود')]"))



    def send_data_in_input_username(self):
        self.send_keys((By.ID,'username'),'09104652470')

    def send_data_in_input_password(self):
        self.send_keys((By.ID,'password'),'A123456789')


    def click_on_button_vorod_after_fill(self):
        self.click((By.CSS_SELECTOR, ".ps-4"))



    # def open_transaction_tab(self):
    #     """باز کردن تب تراکنش"""
    #     self.click((By.CSS_SELECTOR, '.gap-x-0'))
    #
    # def select_transaction_type(self):
    #     """انتخاب نوع تراکنش"""
    #     self.click((By.CSS_SELECTOR, '.transaction-type-selector'))
    #
    # def click_on_button_bazarha(self):
    #     """کلیک روی دکمه بازارها"""
    #     self.click((By.CSS_SELECTOR, '.market-button-selector'))
    #
    # def click_on_tab_montakhab_ha(self):
    #     """کلیک روی تب منتخب‌ها"""
    #     self.click((By.XPATH, "//div[@class='w-full mb-4 relative']//button[contains(.,'منتخب‌ها')]"))
    #
    #
    # def click_on_tab_arz_ha(self):
    #     """کلیک روی تب ارزها"""
    #     self.click((By.XPATH, "//div[@class='flex scrollbar-hidden items-center relative "
    #                                               "w-full']//span[contains(.,'ارزها')]"))
    #
    # def click_on_tab_tomani(self):
    #     """کلیک روی تب تومانی"""
    #     self.click((By.XPATH, "//div[@class='flex scrollbar-hidden items-center relative "
    #                                               "w-full']//span[contains(.,'تومانی')]"))
    #
    # def click_on_tab_teteri(self):
    #     """کلیک روی تب تتری"""
    #     self.click((By.XPATH, "//div[@class='flex scrollbar-hidden items-center relative "
    #                                               "w-full']//span[contains(.,'تتری')]"))
    #
    # def click_on_tab_ahrom_dar(self):
    #     self.click((By.XPATH,"//div[@class='flex scrollbar-hidden items-center relative "
    #                                               "w-full']//span[contains(.,'معامله اهرم‌دار')]"))
    #     """کلیک روی تب معامله اهرم‌دار"""

