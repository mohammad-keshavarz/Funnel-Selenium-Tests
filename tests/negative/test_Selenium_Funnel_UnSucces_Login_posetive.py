#import pytest
import time

from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver import ActionChains, Keys
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
    username_input = driver.find_element(By.ID, 'username')
    actions = ActionChains(driver)
    actions.double_click(username_input).perform()
    actions.send_keys(Keys.BACKSPACE * 15)
    actions.perform()
    time.sleep(2)
    print("\n")



    login_page.send_data_in_input_username_with_char_english_in_first_numumber()
    print("بررسی ورود شماره تلفن  همراه با کاراکتر انگلیسی  در ابندای شماره نلفن ")
    send_data_in_input_username_with_char_english_in_first_numumber = driver.find_elements(By.CSS_SELECTOR, ".input-error-message")
    assert len(send_data_in_input_username_with_char_english_in_first_numumber) > 0, "Username error message not displayed"
    assert send_data_in_input_username_with_char_english_in_first_numumber[0].is_displayed(), "Username error message is not visible"
    print("error message web site display  : ", send_data_in_input_username_with_char_english_in_first_numumber[0].text)
    username_input = driver.find_element(By.ID, 'username')
    actions = ActionChains(driver)
    actions.double_click(username_input).perform()
    actions.send_keys(Keys.BACKSPACE * 15)
    actions.perform()
    time.sleep(2)
    print("\n")



    login_page.send_data_in_input_username_with_Entering_a_number_that_does_not_start_with_09()
    print("بررسی ورود شماره تلفن  همراه با 9 رقم ")
    send_data_in_input_username_withEntering_a_number_that_does_not_start_with_09 = driver.find_elements(By.CSS_SELECTOR, ".input-error-message")
    assert len(send_data_in_input_username_withEntering_a_number_that_does_not_start_with_09) > 0, "Username error message not displayed"
    assert send_data_in_input_username_withEntering_a_number_that_does_not_start_with_09[0].is_displayed(), "Username error message is not visible"
    print("error message web site display  : ", send_data_in_input_username_withEntering_a_number_that_does_not_start_with_09[0].text)
    username_input = driver.find_element(By.ID, 'username')
    actions = ActionChains(driver)
    actions.double_click(username_input).perform()
    actions.send_keys(Keys.BACKSPACE * 15)
    actions.perform()
    time.sleep(2)
    print("\n")



    login_page.send_data_in_input_username_with_null_number()
    print("بررسی عدم ورود شماره تلفن ")
    send_data_in_input_username_with_null_number = driver.find_elements(
    By.CSS_SELECTOR, ".input-error-message")
    assert len(
        send_data_in_input_username_with_null_number) > 0, "Username error message not displayed"
    assert send_data_in_input_username_with_null_number[
    0].is_displayed(), "Username error message is not visible"
    print("error message web site display  : ",
    send_data_in_input_username_with_null_number[0].text)
    username_input = driver.find_element(By.ID, 'username')
    actions = ActionChains(driver)
    actions.double_click(username_input).perform()
    actions.send_keys(Keys.BACKSPACE * 15)
    actions.perform()
    time.sleep(2)
    print("\n")












    login_page.send_data_in_input_password()
    login_page.click_on_button_vorod_after_fill()
#
#



