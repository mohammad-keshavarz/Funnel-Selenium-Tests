# import time
# import traceback
# from selenium.common.exceptions import NoSuchElementException, TimeoutException
# from selenium.webdriver import ActionChains, Keys
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from pages.negative.negative_login_page import negative_login_page
# from confdriver.conftest import driver
#
#
# def test_negative_scenario(driver):
#
#     login_page = negative_login_page(driver)
#     login_page.click_on_Button_Vorod()
#     print("بررسی کلیک کردن روی دکمه ورود")
#
#     try:
#
#         login_button = WebDriverWait(driver, 10).until(
#             EC.presence_of_element_located((By.XPATH, "//span[contains(.,'ورود')]"))
#         )
#
#         # بررسی نمایش و فعال بودن دکمه
#         if login_button.is_displayed() and login_button.is_enabled():
#             print(" دکمه ورود پیدا شد و قابل کلیک است")
#             print("\n")
#         else:
#             print("⚠️ دکمه ورود پیدا شد اما یا قابل مشاهده نیست یا کلیک‌پذیر نیست")
#             assert False, "Button 'Vorod' is not visible or not clickable"
#
#     except NoSuchElementException:
#         print("❌ خطا: دکمه ورود پیدا نشد")
#
#         assert False, "Button 'Vorod' not found"
#
#     except TimeoutException:
#         print("❌ خطا: دکمه ورود بارگذاری نشد به موقع")
#         assert False, "Button 'Vorod' did not load in time"
#
#
#
#
#
#
#     login_page.send_data_in_input_username_with_9_number()
#     print("بررسی ورود شماره تلفن همراه با ۹ کاراکتر")
#
#     send_data_in_input_username_with_9_number = driver.find_elements(By.CSS_SELECTOR, ".input-error-message")
#     login_page.send_data_in_input_password()
#     login_page.click_on_button_vorod_after_fill()
#
#
#     try:
#         assert len(send_data_in_input_username_with_9_number) > 0
#     except AssertionError:
#         print("خطا: لطفا تلفن همراه/آدرس ایمیل را به صورت صحیح وارد کنید")
#
#         print(traceback.format_exc())
#
#     try:
#         assert send_data_in_input_username_with_9_number[0].is_displayed()
#     except (AssertionError, IndexError):
#         print("خطا: پیام خطای نام کاربری قابل مشاهده نیست یا عنصر یافت نشد")
#         print(traceback.format_exc())
#     else:
#         print("error message web site display  : ", send_data_in_input_username_with_9_number[0].text)
#
#     try:
#         username_input = driver.find_element(By.ID, 'username')
#         pasword_input = driver.find_element(By.ID,'password')
#         actions = ActionChains(driver)
#         actions.double_click(username_input).perform()
#         actions.send_keys(Keys.BACKSPACE * 15)
#         actions.double_click(pasword_input).perform()
#         actions.send_keys(Keys.BACKSPACE * 15)
#         actions.perform()
#         time.sleep(1)
#     except Exception as e:
#         print("خطا در پاک کردن فیلد نام کاربری:", str(e))
#         print(traceback.format_exc())
#
#     print("\n")
#
#     login_page.send_data_in_input_username_with_char_english_in_first_numumber()
#     print("بررسی ورود شماره تلفن همراه با کاراکتر انگلیسی در ابتدای شماره تلفن")
#
#     send_data_in_input_username_with_char_english_in_first_numumber = driver.find_elements(By.CSS_SELECTOR,
#                                                                                            ".input-error-message")
#     login_page.send_data_in_input_password()
#     login_page.click_on_button_vorod_after_fill()
#     try:
#         assert len(send_data_in_input_username_with_char_english_in_first_numumber) > 0
#     except AssertionError:
#         print("خطا: لطفا تلفن همراه/آدرس ایمیل را به صورت صحیح وارد کنید")
#
#         print(traceback.format_exc())
#
#     try:
#         assert send_data_in_input_username_with_char_english_in_first_numumber[0].is_displayed()
#     except (AssertionError, IndexError):
#         print("خطا: پیام خطای نام کاربری قابل مشاهده نیست یا عنصر یافت نشد")
#         print(traceback.format_exc())
#     else:
#         print("error message web site display  : ",
#               send_data_in_input_username_with_char_english_in_first_numumber[0].text)
#
#     try:
#         username_input = driver.find_element(By.ID, 'username')
#         pasword_input = driver.find_element(By.ID, 'password')
#         actions = ActionChains(driver)
#         actions.double_click(username_input).perform()
#         actions.send_keys(Keys.BACKSPACE * 15)
#         actions.double_click(pasword_input).perform()
#         actions.send_keys(Keys.BACKSPACE * 15)
#         actions.perform()
#         time.sleep(1)
#     except Exception as e:
#         print("خطا در پاک کردن فیلد نام کاربری:", str(e))
#         print(traceback.format_exc())
#
#     print("\n")
#
#
#     login_page.send_data_in_input_username_with_Entering_a_number_that_does_not_start_with_09()
#     print("بررسی ورود شماره تلفن همراه با 9 رقم")
#
#     send_data_in_input_username_withEntering_a_number_that_does_not_start_with_09 = driver.find_elements(
#         By.CSS_SELECTOR, ".input-error-message")
#     login_page.send_data_in_input_password()
#     login_page.click_on_button_vorod_after_fill()
#     try:
#         assert len(send_data_in_input_username_withEntering_a_number_that_does_not_start_with_09) > 0
#     except AssertionError:
#         print("خطا: لطفا تلفن همراه/آدرس ایمیل را به صورت صحیح وارد کنید")
#
#         print(traceback.format_exc())
#
#     try:
#         assert send_data_in_input_username_withEntering_a_number_that_does_not_start_with_09[0].is_displayed()
#     except (AssertionError, IndexError):
#         print("خطا: پیام خطای نام کاربری قابل مشاهده نیست یا عنصر یافت نشد")
#         print(traceback.format_exc())
#     else:
#         print("error message web site display  : ",
#               send_data_in_input_username_withEntering_a_number_that_does_not_start_with_09[0].text)
#
#     try:
#         username_input = driver.find_element(By.ID, 'username')
#         pasword_input = driver.find_element(By.ID, 'password')
#         actions = ActionChains(driver)
#         actions.double_click(username_input).perform()
#         actions.send_keys(Keys.BACKSPACE * 15)
#         actions.double_click(pasword_input).perform()
#         actions.send_keys(Keys.BACKSPACE * 15)
#         actions.perform()
#         time.sleep(1)
#     except Exception as e:
#         print("خطا در پاک کردن فیلد نام کاربری:", str(e))
#         print(traceback.format_exc())
#
#     print("\n")
#
#     login_page.send_data_in_input_username_with_null_number()
#     print("بررسی عدم ورود شماره تلفن")
#
#     send_data_in_input_username_with_null_number = driver.find_elements(By.CSS_SELECTOR, ".input-error-message")
#     login_page.send_data_in_input_password()
#     login_page.click_on_button_vorod_after_fill()
#     try:
#         assert len(send_data_in_input_username_with_null_number) > 0
#     except AssertionError:
#         print("خطا: لطفا تلفن همراه/آدرس ایمیل را به صورت صحیح وارد کنید")
#
#         print(traceback.format_exc())
#
#     try:
#         assert send_data_in_input_username_with_null_number[0].is_displayed()
#     except (AssertionError, IndexError):
#         print("خطا: پیام خطای نام کاربری قابل مشاهده نیست یا عنصر یافت نشد")
#         print(traceback.format_exc())
#     else:
#         print("error message web site display  : ", send_data_in_input_username_with_null_number[0].text)
#
#     try:
#         username_input = driver.find_element(By.ID, 'username')
#         pasword_input = driver.find_element(By.ID, 'password')
#         actions = ActionChains(driver)
#         actions.double_click(username_input).perform()
#         actions.send_keys(Keys.BACKSPACE * 15)
#         actions.double_click(pasword_input).perform()
#         actions.send_keys(Keys.BACKSPACE * 15)
#         actions.perform()
#         time.sleep(1)
#     except Exception as e:
#         print(" وارد کردن تلفن همراه الزامی است:", str(e))
#         print(traceback.format_exc())
#
#     print("\n")
#
#     login_page.send_data_in_input_username_with_Enterin_the_phone_number_in_reverse()
#     print("بررسی ورود شماره تلفن برعکس")
#
#     send_data_in_input_username_with_Enterin_the_phone_number_in_reverse = driver.find_elements(By.CSS_SELECTOR,
#                                                                                                 ".input-error-message")
#     login_page.send_data_in_input_password()
#     login_page.click_on_button_vorod_after_fill()
#     try:
#         assert len(send_data_in_input_username_with_Enterin_the_phone_number_in_reverse) > 0
#     except AssertionError:
#         print("خطا: لطفا تلفن همراه/آدرس ایمیل را به صورت صحیح وارد کنید")
#
#         print(traceback.format_exc())
#
#     try:
#         assert send_data_in_input_username_with_Enterin_the_phone_number_in_reverse[0].is_displayed()
#     except (AssertionError, IndexError):
#         print("خطا: پیام خطای نام کاربری قابل مشاهده نیست یا عنصر یافت نشد")
#         print(traceback.format_exc())
#     else:
#         print("error message web site display  : ",
#               send_data_in_input_username_with_Enterin_the_phone_number_in_reverse[0].text)
#
#     try:
#         username_input = driver.find_element(By.ID, 'username')
#         pasword_input = driver.find_element(By.ID, 'password')
#         actions = ActionChains(driver)
#         actions.double_click(username_input).perform()
#         actions.send_keys(Keys.BACKSPACE * 15)
#         actions.double_click(pasword_input).perform()
#         actions.send_keys(Keys.BACKSPACE * 15)
#         actions.perform()
#         time.sleep(1)
#     except Exception as e:
#         print("خطا در پاک کردن فیلد نام کاربری:", str(e))
#         print(traceback.format_exc())
#
#     print("\n")
#
#     login_page.send_data_in_input_username_with_Entering_a_phone_number_with_special_characters()
#     print("بررسی ورود کاراکتر های ویژه در تلفن همراه")
#
#     send_data_in_input_username_with_Entering_a_phone_number_with_special_characters = driver.find_elements(
#         By.CSS_SELECTOR, ".input-error-message")
#     login_page.send_data_in_input_password()
#     login_page.click_on_button_vorod_after_fill()
#     try:
#         assert len(send_data_in_input_username_with_Entering_a_phone_number_with_special_characters) > 0
#     except AssertionError:
#         print("خطا: لطفا تلفن همراه/آدرس ایمیل را به صورت صحیح وارد کنید")
#
#         print(traceback.format_exc())
#
#     try:
#         assert send_data_in_input_username_with_Entering_a_phone_number_with_special_characters[0].is_displayed()
#     except (AssertionError, IndexError):
#         print("خطا: پیام خطای نام کاربری قابل مشاهده نیست یا عنصر یافت نشد")
#         print(traceback.format_exc())
#     else:
#         print("error message web site display  : ",
#               send_data_in_input_username_with_Entering_a_phone_number_with_special_characters[0].text)
#
#     try:
#         username_input = driver.find_element(By.ID, 'username')
#         pasword_input = driver.find_element(By.ID, 'password')
#         actions = ActionChains(driver)
#         actions.double_click(username_input).perform()
#         actions.send_keys(Keys.BACKSPACE * 15)
#         actions.double_click(pasword_input).perform()
#         actions.send_keys(Keys.BACKSPACE * 15)
#         actions.perform()
#         time.sleep(1)
#     except Exception as e:
#         print("خطا در پاک کردن فیلد نام کاربری:", str(e))
#         print(traceback.format_exc())
#
#     print("\n")
#
#     login_page.send_data_in_input_username_with_Entering_number_0()
#     print("بررسی ورود شماره تلفن با ارقام 0")
#
#     send_data_in_input_username_with_Entering_number_0 = driver.find_elements(By.CSS_SELECTOR, ".input-error-message")
#     login_page.send_data_in_input_password()
#     login_page.click_on_button_vorod_after_fill()
#     try:
#         assert len(send_data_in_input_username_with_Entering_number_0) > 0
#     except AssertionError:
#         print("خطا:لطفا تلفن همراه/آدرس ایمیل را به صورت صحیح وارد کنید")
#
#         print(traceback.format_exc())
#
#     try:
#         assert send_data_in_input_username_with_Entering_number_0[0].is_displayed()
#     except (AssertionError, IndexError):
#         print("خطا: پیام خطای نام کاربری قابل مشاهده نیست یا عنصر یافت نشد")
#         print(traceback.format_exc())
#     else:
#         print("error message web site display  : ", send_data_in_input_username_with_Entering_number_0[0].text)
#
#     try:
#         username_input = driver.find_element(By.ID, 'username')
#         pasword_input = driver.find_element(By.ID, 'password')
#         actions = ActionChains(driver)
#         actions.double_click(username_input).perform()
#         actions.send_keys(Keys.BACKSPACE * 15)
#         actions.double_click(pasword_input).perform()
#         actions.send_keys(Keys.BACKSPACE * 15)
#         actions.perform()
#         time.sleep(1)
#     except Exception as e:
#         print("خطا در پاک کردن فیلد نام کاربری:", str(e))
#         print(traceback.format_exc())
#
#     print("\n")
#
#     login_page.send_data_in_input_username_with_sql_injection_queri_1()
#     print("بررسی ورود کد اس کیو ال اینجکشن شماره : 1")
#
#     send_data_in_input_username_with_sql_injection_queri_1 = driver.find_elements(By.CSS_SELECTOR,
#                                                                                   ".input-error-message")
#     login_page.send_data_in_input_password()
#     login_page.click_on_button_vorod_after_fill()
#     try:
#         assert len(send_data_in_input_username_with_sql_injection_queri_1) > 0
#     except AssertionError:
#         print("خطا: لطفا تلفن همراه/آدرس ایمیل را به صورت صحیح وارد کنید")
#
#         print(traceback.format_exc())
#
#     try:
#         assert send_data_in_input_username_with_sql_injection_queri_1[0].is_displayed()
#     except (AssertionError, IndexError):
#         print("خطا: پیام خطای نام کاربری قابل مشاهده نیست یا عنصر یافت نشد")
#         print(traceback.format_exc())
#     else:
#         print("error message web site display  : ", send_data_in_input_username_with_sql_injection_queri_1[0].text)
#
#     try:
#         username_input = driver.find_element(By.ID, 'username')
#         pasword_input = driver.find_element(By.ID, 'password')
#         actions = ActionChains(driver)
#         actions.double_click(username_input).perform()
#         actions.send_keys(Keys.BACKSPACE * 15)
#         actions.double_click(pasword_input).perform()
#         actions.send_keys(Keys.BACKSPACE * 15)
#         actions.perform()
#         time.sleep(1)
#     except Exception as e:
#         print("خطا در پاک کردن فیلد نام کاربری:", str(e))
#         print(traceback.format_exc())
#
#     print("\n")
#
#     login_page.send_data_in_input_username_with_sql_injection_queri_2()
#     print("بررسی ورود کد اس کیو ال اینجکشن شماره : 2")
#
#     send_data_in_input_username_with_sql_injection_queri_2 = driver.find_elements(By.CSS_SELECTOR,
#                                                                                   ".input-error-message")
#     login_page.send_data_in_input_password()
#     login_page.click_on_button_vorod_after_fill()
#     try:
#         assert len(send_data_in_input_username_with_sql_injection_queri_2) > 0
#     except AssertionError:
#         print("خطا: لطفا تلفن همراه/آدرس ایمیل را به صورت صحیح وارد کنید")
#
#         print(traceback.format_exc())
#
#     try:
#         assert send_data_in_input_username_with_sql_injection_queri_2[0].is_displayed()
#     except (AssertionError, IndexError):
#         print("خطا: پیام خطای نام کاربری قابل مشاهده نیست یا عنصر یافت نشد")
#         print(traceback.format_exc())
#     else:
#         print("error message web site display  : ", send_data_in_input_username_with_sql_injection_queri_2[0].text)
#
#     try:
#         username_input = driver.find_element(By.ID, 'username')
#         pasword_input = driver.find_element(By.ID, 'password')
#         actions = ActionChains(driver)
#         actions.double_click(username_input).perform()
#         actions.send_keys(Keys.BACKSPACE * 15)
#         actions.double_click(pasword_input).perform()
#         actions.send_keys(Keys.BACKSPACE * 15)
#         actions.perform()
#         time.sleep(1)
#     except Exception as e:
#         print("خطا در پاک کردن فیلد نام کاربری:", str(e))
#         print(traceback.format_exc())
#
#     print("\n")
#
#     # login_page.send_data_in_input_password()
#     # login_page.click_on_button_vorod_after_fill()


import traceback
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from pages.negative.negative_login_page import negative_login_page
from confdriver.conftest import driver

def test_validate_username_with_9_digits(driver):
    login_page = negative_login_page(driver)

    try:

        login_page.click_on_Button_Vorod()
        negative_login_page.send_data_in_input_username_with_9_number(driver)
        time.sleep(3)
        negative_login_page.send_data_in_input_password(driver)
    #     print("بررسی ورود شماره تلفن همراه با ۹ کاراکتر")
    #     error_messages = driver.find_elements(By.CSS_SELECTOR, ".input-error-message")
    #     if len(error_messages) == 0:
    #         print("خطا: لطفا تلفن همراه/آدرس ایمیل را به صورت صحیح وارد کنید")
    #     elif not error_messages[0].is_displayed():
    #         print("خطا: پیام خطای نام کاربری قابل مشاهده نیست یا عنصر یافت نشد")
    #     else:
    #         print("error message web site display  :", error_messages[0].text)
    # except Exception as e:
    #     print("خطای غیرمنتظره: " + str(e))
    #     print(traceback.format_exc())
    finally:
        clear_input_fields(driver)

# def test_validate_username_with_char_english_in_first(driver, login_page):
#     try:
#         login_page.send_data_in_input_username_with_char_english_in_first_numumber()
#         print("بررسی ورود شماره تلفن همراه با کاراکتر انگلیسی در ابتدای شماره تلفن")
#         error_messages = driver.find_elements(By.CSS_SELECTOR, ".input-error-message")
#         if len(error_messages) == 0:
#             print("خطا: لطفا تلفن همراه/آدرس ایمیل را به صورت صحیح وارد کنید")
#         elif not error_messages[0].is_displayed():
#             print("خطا: پیام خطای نام کاربری قابل مشاهده نیست یا عنصر یافت نشد")
#         else:
#             print("error message web site display  :", error_messages[0].text)
#     except Exception as e:
#         print("خطای غیرمنتظره: " + str(e))
#         print(traceback.format_exc())
#     finally:
#         clear_input_fields(driver)
#
# def test_validate_username_with_invalid_start(driver, login_page):
#     try:
#         login_page.send_data_in_input_username_with_Entering_a_number_that_does_not_start_with_09()
#         print("بررسی ورود شماره تلفن همراه که با 09 شروع نمی‌شود")
#         error_messages = driver.find_elements(By.CSS_SELECTOR, ".input-error-message")
#         if len(error_messages) == 0:
#             print("خطا: لطفا تلفن همراه/آدرس ایمیل را به صورت صحیح وارد کنید")
#         elif not error_messages[0].is_displayed():
#             print("خطا: پیام خطای نام کاربری قابل مشاهده نیست یا عنصر یافت نشد")
#         else:
#             print("error message web site display  :", error_messages[0].text)
#     except Exception as e:
#         print("خطای غیرمنتظره: " + str(e))
#         print(traceback.format_exc())
#     finally:
#         clear_input_fields(driver)
#
# def test_validate_username_with_null_number(driver, login_page):
#     try:
#         login_page.send_data_in_input_username_with_null_number()
#         print("بررسی عدم ورود شماره تلفن")
#         error_messages = driver.find_elements(By.CSS_SELECTOR, ".input-error-message")
#         if len(error_messages) == 0:
#             print("خطا: لطفا تلفن همراه/آدرس ایمیل را به صورت صحیح وارد کنید")
#         elif not error_messages[0].is_displayed():
#             print("خطا: پیام خطای نام کاربری قابل مشاهده نیست یا عنصر یافت نشد")
#         else:
#             print("error message web site display  :", error_messages[0].text)
#     except Exception as e:
#         print("خطای غیرمنتظره: " + str(e))
#         print(traceback.format_exc())
#     finally:
#         clear_input_fields(driver)
#
# def test_validate_username_with_reverse_number(driver, login_page):
#     try:
#         login_page.send_data_in_input_username_with_Enterin_the_phone_number_in_reverse()
#         print("بررسی ورود شماره تلفن برعکس")
#         error_messages = driver.find_elements(By.CSS_SELECTOR, ".input-error-message")
#         if len(error_messages) == 0:
#             print("خطا: لطفا تلفن همراه/آدرس ایمیل را به صورت صحیح وارد کنید")
#         elif not error_messages[0].is_displayed():
#             print("خطا: پیام خطای نام کاربری قابل مشاهده نیست یا عنصر یافت نشد")
#         else:
#             print("error message web site display  :", error_messages[0].text)
#     except Exception as e:
#         print("خطای غیرمنتظره: " + str(e))
#         print(traceback.format_exc())
#     finally:
#         clear_input_fields(driver)
#
# def test_validate_username_with_special_chars(driver, login_page):
#     try:
#         login_page.send_data_in_input_username_with_Entering_a_phone_number_with_special_characters()
#         print("بررسی ورود کاراکترهای ویژه در تلفن همراه")
#         error_messages = driver.find_elements(By.CSS_SELECTOR, ".input-error-message")
#         if len(error_messages) == 0:
#             print("خطا: لطفا تلفن همراه/آدرس ایمیل را به صورت صحیح وارد کنید")
#         elif not error_messages[0].is_displayed():
#             print("خطا: پیام خطای نام کاربری قابل مشاهده نیست یا عنصر یافت نشد")
#         else:
#             print("error message web site display  :", error_messages[0].text)
#     except Exception as e:
#         print("خطای غیرمنتظره: " + str(e))
#         print(traceback.format_exc())
#     finally:
#         clear_input_fields(driver)
#
# def test_validate_username_with_all_zeros(driver, login_page):
#     try:
#         login_page.send_data_in_input_username_with_Entering_number_0()
#         print("بررسی ورود شماره تلفن با ارقام 0")
#         error_messages = driver.find_elements(By.CSS_SELECTOR, ".input-error-message")
#         if len(error_messages) == 0:
#             print("خطا: لطفا تلفن همراه/آدرس ایمیل را به صورت صحیح وارد کنید")
#         elif not error_messages[0].is_displayed():
#             print("خطا: پیام خطای نام کاربری قابل مشاهده نیست یا عنصر یافت نشد")
#         else:
#             print("error message web site display  :", error_messages[0].text)
#     except Exception as e:
#         print("خطای غیرمنتظره: " + str(e))
#         print(traceback.format_exc())
#     finally:
#         clear_input_fields(driver)
#
# def test_validate_username_with_sql_injection_1(driver, login_page):
#     try:
#         login_page.send_data_in_input_username_with_sql_injection_queri_1()
#         print("بررسی ورود کد SQL Injection شماره 1")
#         error_messages = driver.find_elements(By.CSS_SELECTOR, ".input-error-message")
#         if len(error_messages) == 0:
#             print("خطا: لطفا تلفن همراه/آدرس ایمیل را به صورت صحیح وارد کنید")
#         elif not error_messages[0].is_displayed():
#             print("خطا: پیام خطای نام کاربری قابل مشاهده نیست یا عنصر یافت نشد")
#         else:
#             print("error message web site display  :", error_messages[0].text)
#     except Exception as e:
#         print("خطای غیرمنتظره: " + str(e))
#         print(traceback.format_exc())
#     finally:
#         clear_input_fields(driver)
#
# def test_validate_username_with_sql_injection_2(driver, login_page):
#     try:
#         login_page.send_data_in_input_username_with_sql_injection_queri_2()
#         print("بررسی ورود کد SQL Injection شماره 2")
#         error_messages = driver.find_elements(By.CSS_SELECTOR, ".input-error-message")
#         if len(error_messages) == 0:
#             print("خطا: لطفا تلفن همراه/آدرس ایمیل را به صورت صحیح وارد کنید")
#         elif not error_messages[0].is_displayed():
#             print("خطا: پیام خطای نام کاربری قابل مشاهده نیست یا عنصر یافت نشد")
#         else:
#             print("error message web site display  :", error_messages[0].text)
#     except Exception as e:
#         print("خطای غیرمنتظره: " + str(e))
#         print(traceback.format_exc())
#     finally:
#         clear_input_fields(driver)

def clear_input_fields(driver):
    try:
        username_input = driver.find_element(By.ID, 'username')
        password_input = driver.find_element(By.ID, 'password')
        actions = ActionChains(driver)
        actions.double_click(username_input).send_keys(Keys.BACKSPACE * 15).perform()
        time.sleep(0.5)
        actions.double_click(password_input).send_keys(Keys.BACKSPACE * 15).perform()
        time.sleep(0.5)
    except Exception as e:
        print("خطا در پاک کردن فیلدهای ورودی:", str(e))
        print(traceback.format_exc())

