import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from pages.trade_page import TradePage
from confdriver.conftest import driver


def test_positive_scenario(driver):
    """تست سناریوی مثبت برای باز کردن تب‌ها و انتخاب گزینه‌ها"""
    print("dirver", driver)
    # ایجاد نمونه‌ای از TradePage
    trade_page = TradePage(driver)
    print("dirver", driver)

    trade_page.click_on_Button_Vorod()
    trade_page.send_data_in_input_username()
    trade_page.send_data_in_input_password()
    trade_page.click_on_button_vorod_after_fill()





    time.sleep(1000)

    # # پیدا کردن عنصر با کلاس. bg-gray-100
    # target_element = driver.find_element(By.CSS_SELECTOR, ".bg-gray-100")
    #
    # # اسکرول به عنصر با استفاده از ActionChains
    # actions = ActionChains(driver)
    # actions.move_to_element(target_element).perform()
    # # کلیک روی دکمه شروع معامله
    # target_element.click()

    # # باز کردن تب تراکنش
    # trade_page.open_transaction_tab()
    #
    #
    # # # انتخاب نوع تراکنش
    # # trade_page.select_transaction_type()
    #
    # # # کلیک روی دکمه بازارها
    # # trade_page.click_on_button_bazarha()
    #
    # # کلیک روی تب منتخب‌ها
    # trade_page.click_on_tab_montakhab_ha()
    #
    # # کلیک روی تب ارزها
    # trade_page.click_on_tab_arz_ha()
    #
    # # کلیک روی تب تومانی
    # trade_page.click_on_tab_tomani()
    #
    # # کلیک روی تب تتری
    # trade_page.click_on_tab_teteri()
    #
    # # کلیک روی تب معامله اهرم‌دار
    # trade_page.click_on_tab_ahrom_dar()

    print("✅ تست مثبت با موفقیت انجام شد.")



