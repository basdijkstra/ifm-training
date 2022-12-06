from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BasePage:

    def __init__(self, driver):
        self._driver = driver
        self._timeout = 10

    def send_keys(self, locator, text):
        WebDriverWait(self._driver, self._timeout).until(ec.element_to_be_clickable(locator))
        self._driver.find_element(*locator).send_keys(text)

    def click(self, locator):
        WebDriverWait(self._driver, self._timeout).until(ec.element_to_be_clickable(locator))
        self._driver.find_element(*locator).click()

    def select(self, locator, value):
        WebDriverWait(self._driver, self._timeout).until(ec.element_to_be_clickable(locator))
        dropdown = Select(self._driver.find_element(*locator))
        dropdown.select_by_visible_text(value)

    def get_element_text(self, locator):
        WebDriverWait(self._driver, self._timeout).until(ec.visibility_of_element_located(locator))
        return self._driver.find_element(*locator).text

    def select_menu_item(self, link_text):
        self.click((By.LINK_TEXT, link_text))
