from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from webdriver_manager.chrome import ChromeDriverManager

from pages.login_page import LoginPage
from pages.accounts_overview_page import AccountsOverviewPage
from pages.request_loan_page import RequestLoanPage


def test_loan_application_is_denied():

    # Open browser
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get('https://parabank.parasoft.com')
    driver.maximize_window()

    # Log in to Parabank
    LoginPage(driver).login_as('john', 'demo')

    # Navigate to Request Loan
    AccountsOverviewPage(driver).select_menu_item('Request Loan')

    # Fill in loan application
    rlp = RequestLoanPage(driver)

    rlp.submit_loan_request('10000', '100', '12345')

    # Assert on loan application result
    assert rlp.get_loan_application_result() == 'Denied'

    # Close browser
    driver.quit()
