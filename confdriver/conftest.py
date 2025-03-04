import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture
def driver():

    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-notifications")
    chrome_driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    chrome_driver.get("https://tabdeal.org/")
    yield chrome_driver
    chrome_driver.quit()
