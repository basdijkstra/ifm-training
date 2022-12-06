from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class RequestLoanPage:

    def __init__(self, driver):
        self._driver = driver
        self._amount = (By.ID, 'amount')
        self._down_payment = (By.ID, 'downPayment')
        self._from_account_id = (By.ID, 'fromAccountId')
        self._apply_now_button = (By.XPATH, '//input[@value=\'Apply Now\']')
        self._loan_status = (By.ID, 'loanStatus')

    def submit_loan_request(self, amount, down_payment, from_account_id):
        send_keys(self._driver, self._amount, amount)
        send_keys(self._driver, self._down_payment, down_payment)
        select(self._driver, self._from_account_id, from_account_id)
        click(self._driver, self._apply_now_button)

    def get_loan_application_result(self):
        return get_element_text(self._driver, self._loan_status)


def send_keys(driver, locator, text):
    WebDriverWait(driver, 10).until(ec.element_to_be_clickable(locator))
    driver.find_element(*locator).send_keys(text)


def click(driver, locator):
    WebDriverWait(driver, 10).until(ec.element_to_be_clickable(locator))
    driver.find_element(*locator).click()


def select(driver, locator, value):
    WebDriverWait(driver, 10).until(ec.element_to_be_clickable(locator))
    dropdown = Select(driver.find_element(*locator))
    dropdown.select_by_visible_text(value)


def get_element_text(driver, locator):
    WebDriverWait(driver, 10).until(ec.visibility_of_element_located(locator))
    return driver.find_element(*locator).text
