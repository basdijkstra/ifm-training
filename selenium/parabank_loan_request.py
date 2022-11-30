from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from webdriver_manager.chrome import ChromeDriverManager


def test_loan_application_is_denied():

    # Open browser
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get('https://parabank.parasoft.com')
    driver.maximize_window()

    # Log in to Parabank
    send_keys(driver, By.NAME, 'username', 'john')
    send_keys(driver, By.NAME, 'password', 'demo')
    click(driver, By.XPATH, '//input[@value=\'Log In\']')

    # Navigate to Request Loan
    click(driver, By.LINK_TEXT, 'Request Loan')

    # Fill in loan application
    send_keys(driver, By.ID, 'amount', '10000')
    send_keys(driver, By.ID, 'downPayment', '100')
    select(driver, By.ID, 'fromAccountId', '12345')
    click(driver, By.XPATH, '//input[@value=\'Apply Now\']')

    # Assert on loan application result
    result = get_element_text(driver, By.ID, 'loanStatus')
    assert result == 'Denied'

    # Close browser
    driver.quit()


def send_keys(driver, locator_strategy, locator, text):
    WebDriverWait(driver, 10).until(ec.element_to_be_clickable((locator_strategy, locator)))
    driver.find_element(locator_strategy, locator).send_keys(text)


def click(driver, locator_strategy, locator):
    WebDriverWait(driver, 10).until(ec.element_to_be_clickable((locator_strategy, locator)))
    driver.find_element(locator_strategy, locator).click()


def select(driver, locator_strategy, locator, value):
    WebDriverWait(driver, 10).until(ec.element_to_be_clickable((locator_strategy, locator)))
    dropdown = Select(driver.find_element(locator_strategy, locator))
    dropdown.select_by_visible_text(value)


def get_element_text(driver, locator_strategy, locator):
    WebDriverWait(driver, 10).until(ec.visibility_of_element_located((locator_strategy, locator)))
    return driver.find_element(locator_strategy, locator).text
