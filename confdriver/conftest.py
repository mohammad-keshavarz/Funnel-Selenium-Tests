import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture
def driver():
    """ایجاد و مقداردهی WebDriver برای تست"""
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-notifications")

    chrome_driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    # باز کردن سایت موردنظر
    chrome_driver.get("https://tabdeal.org/")  # ✅ این خط مشخص می‌کند که وب‌سایت چه باشد

    yield chrome_driver  # بازگرداندن WebDriver برای استفاده در تست‌ها

    chrome_driver.quit()  # بستن مرورگر پس از پایان تست
