from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class AccountsOverviewPage:

    def __init__(self, driver):
        self._driver = driver

    def select_menu_item(self, link_text):
        click(self._driver, (By.LINK_TEXT, link_text))


def click(driver, locator):
    WebDriverWait(driver, 10).until(ec.element_to_be_clickable(locator))
    driver.find_element(*locator).click()
