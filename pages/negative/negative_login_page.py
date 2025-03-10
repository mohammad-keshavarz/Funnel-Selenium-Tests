from selenium.webdriver.common.by import By
from base_action.base_action import BaseActionLocator



class Negative_login_page(BaseActionLocator):

    def __init__(self, driver):
        super().__init__(driver)


    def click_on_Button_Vorod_negative_login(self):
        self.click((By.XPATH, "//span[contains(.,'ورود')]"))

    def send_data_in_input_username_with_9_number_negative_login(self):
        self.send_keys((By.ID, 'username'), '091046524')

    def send_data_in_input_username_with_char_english_in_first_number_negative_login(self):
        self.send_keys((By.ID, 'username'), 'abc05912215')

    def send_data_in_input_username_with_Entering_a_number_that_does_not_start_with_09_negative_login(self):
        self.send_keys((By.ID, 'username'), '035105912215')

    def send_data_in_input_username_with_null_number_negative_login(self):
        self.send_keys((By.ID, 'username'), '')

    def send_data_in_input_username_with_Enter_in_the_phone_number_in_reverse_negative_login(self):
        self.send_keys((By.ID, 'username'), '59122150910')

    def send_data_in_input_username_with_Entering_a_phone_number_with_special_characters_negative_login(self):
        self.send_keys((By.ID, 'username'), '0910@5912215')

    def send_data_in_input_username_with_Enter_in_number_0_negative_login(self):
        self.send_keys((By.ID, 'username'), '00000000000')

    def send_data_in_input_username_with_sql_injection_queri_1_negative_login(self):
        self.send_keys((By.ID, 'username'), "SELECT * FROM users WHERE phone_number = 'input_value';")

    def send_data_in_input_username_with_sql_injection_queri_2_negative_login(self):
        self.send_keys((By.ID, 'username'), "SELECT * FROM users WHERE phone_number = '' OR '1'='1';")

    def send_data_in_input_password_negative_login(self):
        self.send_keys((By.ID, 'password'), 'A123456789')

    def click_on_button_vorod_after_fill_negative_login(self):
        self.click((By.CSS_SELECTOR, ".ps-4"))





