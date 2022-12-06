from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self._username = (By.NAME, 'username')
        self._password = (By.NAME, 'password')
        self._login_button = (By.XPATH, '//input[@value=\'Log In\']')

    def login_as(self, username, password):
        self.send_keys(self._username, username)
        self.send_keys(self._password, password)
        self.click(self._login_button)
