from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

def open_tabs():
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

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    try:
        driver.get("https://tabdeal.org/")

        # انتظار داینامیک برای بارگذاری لوگو
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "[alt='tabdeal-logo']")))

        # انتظار داینامیک برای بارگذاری عنصر با کلاس. bg-gray-100
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".bg-gray-100")))

        # پیدا کردن عنصر با کلاس. bg-gray-100
        target_element = driver.find_element(By.CSS_SELECTOR, ".bg-gray-100")

        # اسکرول به عنصر با استفاده از ActionChains
        actions = ActionChains(driver)
        actions.move_to_element(target_element).perform()

        # کلیک روی دکمه شروع معامله (اختیاری)
        target_element.click()

        # انتظار داینامیک برای قابل کلیک شدن عنصر با کلاس .gap-x-0
        btn_bazar_element = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".gap-x-0"))
        )
        btn_bazar_element.click()

        tab_arz_ha = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@class='flex scrollbar-hidden items-center relative "
                                                  "w-full']//span[contains(.,'ارزها')]"))
        )
        tab_arz_ha.click()

        tab_tomani = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@class='flex scrollbar-hidden items-center relative "
                                                  "w-full']//span[contains(.,'تومانی')]"))
        )
        tab_tomani.click()

        tab_teter = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@class='flex scrollbar-hidden items-center relative "
                                                  "w-full']//span[contains(.,'تتری')]"))
        )
        tab_teter.click()

        tab_mamele_ahromdar = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@class='flex scrollbar-hidden items-center relative "
                                                  "w-full']//span[contains(.,'معامله اهرم‌دار')]"))
        )
        tab_mamele_ahromdar.click()

    finally:
        print( "اتمام تست . همه تست ها با موفقیت اجرا شدند ")

        # بستن مرورگر
        driver.quit()

# اجرای تابع
open_tabs()
