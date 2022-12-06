from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class LoginPage:

    def __init__(self, driver):
        self._driver = driver
        self._username = (By.NAME, 'username')
        self._password = (By.NAME, 'password')
        self._login_button = (By.XPATH, '//input[@value=\'Log In\']')

    def login_as(self, username, password):
        send_keys(self._driver, self._username, username)
        send_keys(self._driver, self._password, password)
        click(self._driver, self._login_button)


def send_keys(driver, locator, text):
    WebDriverWait(driver, 10).until(ec.element_to_be_clickable(locator))
    driver.find_element(*locator).send_keys(text)


def click(driver, locator):
    WebDriverWait(driver, 10).until(ec.element_to_be_clickable(locator))
    driver.find_element(*locator).click()
