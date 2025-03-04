import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


def test_positive_scenario():
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-notifications")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    try:
        driver.get("https://tabdeal.org/")
        time.sleep(3)

        register_button = driver.find_element(By.XPATH, "//span[contains(.,'ثبت‌نام')]")
        register_button.click()
        time.sleep(1)

        username_field = driver.find_element(By.CSS_SELECTOR, "[placeholder='09xxxxxxxx']")
        time.sleep(2)
        username_field.clear()
        username_field.send_keys("09104652471")
        time.sleep(2)

        password_field = driver.find_element(By.CSS_SELECTOR, "[placeholder='تعیین رمز عبور']")
        password_field.send_keys("root..root007")

        register_button = driver.find_element(By.XPATH, "//span[@class='flex items-center justify-center gap-x-2 w-full whitespace-nowrap py-2 ps-4 pe-4']")
        register_button.click()

        time.sleep(25)

    finally:
        driver.quit()
