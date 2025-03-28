import time
from selenium.webdriver.common.by import By
from pages.negative.negative_login_page import Negative_login_page
from confdriver.conftest import driver



def test_validate_username_with_9_digits(driver):
    negative_login_page = Negative_login_page(driver)

    negative_login_page.click_on_Button_Vorod_negative_login()
    negative_login_page.send_data_in_input_username_with_9_number_negative_login()
    negative_login_page.send_data_in_input_password_negative_login()
    negative_login_page.click_on_button_vorod_after_fill_negative_login()

    try:
        error_element = driver.find_element(By.CSS_SELECTOR, ".input-error-message")
        error_text = error_element.text.strip()


        if error_text == "لطفا تلفن همراه/آدرس ایمیل را به صورت صحیح وارد کنید":
            print(f"پیام خطا: {error_text}")
        else:
            print(f"پیام خطا شناسایی شد اما مقدار آن متفاوت است: {error_text}")

    except:
        print(" باتوجه به منفی بودن سناریوها هیچ پیام خطایی برای فیلد (تلفن همراه/یوزرنیم) نمایش داده نشده است.")

def test_send_data_in_input_username_with_char_english_in_first_number_negative_login(driver):
    negative_login_page = Negative_login_page(driver)

    negative_login_page.click_on_Button_Vorod_negative_login()
    negative_login_page.send_data_in_input_username_with_char_english_in_first_number_negative_login()
    negative_login_page.send_data_in_input_password_negative_login()
    negative_login_page.click_on_button_vorod_after_fill_negative_login()

    try:
        error_element = driver.find_element(By.CSS_SELECTOR, ".input-error-message")
        error_text = error_element.text.strip()

        if error_text == "لطفا تلفن همراه/آدرس ایمیل را به صورت صحیح وارد کنید":
            print(f"پیام خطا: {error_text}")
        else:
            print(f"پیام خطا شناسایی شد اما مقدار آن متفاوت است: {error_text}")

    except:
        print(" باتوجه به منفی بودن سناریوها هیچ پیام خطایی برای فیلد (تلفن همراه/یوزرنیم) نمایش داده نشده است.")

def test_send_data_in_input_username_with_Entering_a_number_that_does_not_start_with_09_negative_login(driver):
    negative_login_page = Negative_login_page(driver)

    negative_login_page.click_on_Button_Vorod_negative_login()
    negative_login_page.send_data_in_input_username_with_Entering_a_number_that_does_not_start_with_09_negative_login()
    negative_login_page.send_data_in_input_password_negative_login()
    negative_login_page.click_on_button_vorod_after_fill_negative_login()

    try:
        error_element = driver.find_element(By.CSS_SELECTOR, ".input-error-message")
        error_text = error_element.text.strip()

        if error_text == "لطفا تلفن همراه/آدرس ایمیل را به صورت صحیح وارد کنید":
            print(f"پیام خطا: {error_text}")
        else:
            print(f"پیام خطا شناسایی شد اما مقدار آن متفاوت است: {error_text}")

    except:
        print(" باتوجه به منفی بودن سناریوها هیچ پیام خطایی برای فیلد (تلفن همراه/یوزرنیم) نمایش داده نشده است.")

def test_send_data_in_input_username_with_null_number_negative_login(driver) :
    negative_login_page = Negative_login_page(driver)
    negative_login_page.click_on_Button_Vorod_negative_login()
    negative_login_page.send_data_in_input_username_with_null_number_negative_login()
    negative_login_page.send_data_in_input_password_negative_login()
    negative_login_page.click_on_button_vorod_after_fill_negative_login()

    try:
        error_element = driver.find_element(By.CSS_SELECTOR, ".input-error-message")
        error_text = error_element.text.strip()

        if error_text == "وارد کردن تلفن همراه الزامی است":

            print(f"پیام خطا: {error_text}")
        else:
            print(f"پیام خطا شناسایی شد اما مقدار آن متفاوت است: {error_text}")

    except:
        print(" باتوجه به منفی بودن سناریوها هیچ پیام خطایی برای فیلد (تلفن همراه/یوزرنیم) نمایش داده نشده است.")

def test_send_data_in_input_username_with_Enter_in_the_phone_number_in_reverse_negative_login(driver):

        negative_login_page = Negative_login_page(driver)
        negative_login_page.click_on_Button_Vorod_negative_login()
        negative_login_page.send_data_in_input_username_with_Enter_in_the_phone_number_in_reverse_negative_login()
        negative_login_page.send_data_in_input_password_negative_login()
        negative_login_page.click_on_button_vorod_after_fill_negative_login()
        try:
            error_element = driver.find_element(By.CSS_SELECTOR, ".input-error-message")
            error_text = error_element.text.strip()

            if error_text == "لطفا تلفن همراه/آدرس ایمیل را به صورت صحیح وارد کنید":
                print(f"پیام خطا: {error_text}")
            else:
                print(f"پیام خطا شناسایی شد اما مقدار آن متفاوت است: {error_text}")

        except:
            print(" باتوجه به منفی بودن سناریوها هیچ پیام خطایی برای فیلد (تلفن همراه/یوزرنیم) نمایش داده نشده است.")

def test_send_data_in_input_username_with_Entering_a_phone_number_with_special_characters_negative_login(driver):
    negative_login_page = Negative_login_page(driver)
    negative_login_page.click_on_Button_Vorod_negative_login()
    negative_login_page.send_data_in_input_username_with_Entering_a_phone_number_with_special_characters_negative_login()
    negative_login_page.send_data_in_input_password_negative_login()
    negative_login_page.click_on_button_vorod_after_fill_negative_login()
    try:
        error_element = driver.find_element(By.CSS_SELECTOR, ".input-error-message")
        error_text = error_element.text.strip()

        if error_text == "لطفا تلفن همراه/آدرس ایمیل را به صورت صحیح وارد کنید":
            print(f"پیام خطا: {error_text}")
        else:
            print(f"پیام خطا شناسایی شد اما مقدار آن متفاوت است: {error_text}")

    except:
        print(" باتوجه به منفی بودن سناریوها هیچ پیام خطایی برای فیلد (تلفن همراه/یوزرنیم) نمایش داده نشده است.")

def send_data_in_input_username_with_Enter_in_number_0_negative_login(driver):
    negative_login_page = Negative_login_page(driver)
    negative_login_page.click_on_Button_Vorod_negative_login()
    negative_login_page.send_data_in_input_username_with_Enter_in_number_0_negative_login()
    negative_login_page.send_data_in_input_password_negative_login()
    negative_login_page.click_on_button_vorod_after_fill_negative_login()
    try:
        error_element = driver.find_element(By.CSS_SELECTOR, ".input-error-message")
        error_text = error_element.text.strip()

        if error_text == "لطفا تلفن همراه/آدرس ایمیل را به صورت صحیح وارد کنید":
            print(f"پیام خطا: {error_text}")
        else:
            print(f"پیام خطا شناسایی شد اما مقدار آن متفاوت است: {error_text}")

    except:
        print(" باتوجه به منفی بودن سناریوها هیچ پیام خطایی برای فیلد (تلفن همراه/یوزرنیم) نمایش داده نشده است.")

def test_end_data_in_input_username_with_sql_injection_queri_1_negative_login(driver):
    negative_login_page = Negative_login_page(driver)
    negative_login_page.click_on_Button_Vorod_negative_login()
    negative_login_page.send_data_in_input_username_with_sql_injection_queri_1_negative_login()
    negative_login_page.send_data_in_input_password_negative_login()
    negative_login_page.click_on_button_vorod_after_fill_negative_login()
    try:
        error_element = driver.find_element(By.CSS_SELECTOR, ".input-error-message")
        error_text = error_element.text.strip()

        if error_text == "لطفا تلفن همراه/آدرس ایمیل را به صورت صحیح وارد کنید":
            print(f"پیام خطا: {error_text}")
        else:
            print(f"پیام خطا شناسایی شد اما مقدار آن متفاوت است: {error_text}")

    except:
        print(" باتوجه به منفی بودن سناریوها هیچ پیام خطایی برای فیلد (تلفن همراه/یوزرنیم) نمایش داده نشده است.")

def teest_send_data_in_input_username_with_sql_injection_queri_2_negative_login(driver):
    negative_login_page = Negative_login_page(driver)
    negative_login_page.click_on_Button_Vorod_negative_login()
    negative_login_page.send_data_in_input_username_with_sql_injection_queri_2_negative_login()
    negative_login_page.send_data_in_input_password_negative_login()
    negative_login_page.click_on_button_vorod_after_fill_negative_login()
    try:
        error_element = driver.find_element(By.CSS_SELECTOR, ".input-error-message")
        error_text = error_element.text.strip()

        if error_text == "لطفا تلفن همراه/آدرس ایمیل را به صورت صحیح وارد کنید":
            print(f"پیام خطا: {error_text}")
        else:
            print(f"پیام خطا شناسایی شد اما مقدار آن متفاوت است: {error_text}")

    except:
        print(" باتوجه به منفی بودن سناریوها هیچ پیام خطایی برای فیلد (تلفن همراه/یوزرنیم) نمایش داده نشده است.")








