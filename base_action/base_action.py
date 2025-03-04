from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BaseActionLocator:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 15)

    def click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def send_keys(self, locator, value):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.clear()  # پاک کردن مقدار قبلی (در صورت وجود)
        element.send_keys(value)