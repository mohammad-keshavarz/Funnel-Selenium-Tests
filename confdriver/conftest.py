
import pytest
import psutil
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def driver():
    # تنظیمات مرورگر
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--disable-popup-blocking")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--disable-animations")
    chrome_options.add_argument("--disable-background-timer-throttling")
    chrome_options.add_argument("--disable-renderer-backgrounding")
    chrome_options.add_argument("--disable-backgrounding-occluded-windows")

    # ایجاد سرویس و راه‌اندازی کروم
    chrome_driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    # آدرس سایت را بارگذاری می‌کنیم
    chrome_driver.get("https://tabdeal.org/")

    # بازگشت driver برای استفاده در تست‌ها
    yield chrome_driver

    # بستن مرورگر فقط کروم باز شده توسط selenium
    chrome_driver.quit()

