#import pytest
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC  # اصلاح ایمپورت

from pages.negative_login_page import negative_login_page
from confdriver.conftest import driver


def test_negative_scenario(driver):
    print("driver test negative", driver)
    login_page = negative_login_page(driver)
    print("driver:", driver)

    # کلیک روی دکمه ورود
    login_page.click_on_Button_Vorod()
    print("بررسی کلیک کردن روی دکمه ورود")

    try:
        # استفاده از WebDriverWait برای اطمینان از بارگذاری دکمه
        login_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[contains(.,'ورود')]"))
        )

        # بررسی نمایش و فعال بودن دکمه
        if login_button.is_displayed() and login_button.is_enabled():
            print(" دکمه ورود پیدا شد و قابل کلیک است")
            print("\n")
        else:
            print("⚠️ دکمه ورود پیدا شد اما یا قابل مشاهده نیست یا کلیک‌پذیر نیست")
            assert False, "Button 'Vorod' is not visible or not clickable"

    except NoSuchElementException:
        print("❌ خطا: دکمه ورود پیدا نشد")

        assert False, "Button 'Vorod' not found"

    except TimeoutException:
        print("❌ خطا: دکمه ورود بارگذاری نشد به موقع")
        assert False, "Button 'Vorod' did not load in time"




    login_page.send_data_in_input_username_with_9_number()
    print("بررسی ورود شماره تلفن  همراه با ۹ کاراکتر")
    send_data_in_input_username_with_9_number = driver.find_elements(By.CSS_SELECTOR, ".input-error-message")
    assert len(send_data_in_input_username_with_9_number) > 0, "Username error message not displayed"
    assert send_data_in_input_username_with_9_number[0].is_displayed(), "Username error message is not visible"
    print("error message web site display  : " , send_data_in_input_username_with_9_number[0].text)

    print("\n")

    login_page.send_data_in_input_username_with_char_english_in_first_numumber()
    print("بررسی ورود شماره تلفن  همراه با کاراکتر انگلیسی  در ابندای شماره نلفن ")
    send_data_in_input_username_with_9_number = driver.find_elements(By.CSS_SELECTOR, ".input-error-message")
    assert len(send_data_in_input_username_with_9_number) > 0, "Username error message not displayed"
    assert send_data_in_input_username_with_9_number[0].is_displayed(), "Username error message is not visible"
    print("error message web site display  : ", send_data_in_input_username_with_9_number[0].text)


    login_page.send_data_in_input_password()
    login_page.click_on_button_vorod_after_fill()





