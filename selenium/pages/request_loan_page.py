from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class RequestLoanPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self._amount = (By.ID, 'amount')
        self._down_payment = (By.ID, 'downPayment')
        self._from_account_id = (By.ID, 'fromAccountId')
        self._apply_now_button = (By.XPATH, '//input[@value=\'Apply Now\']')
        self._loan_status = (By.ID, 'loanStatus')

    def submit_loan_request(self, amount, down_payment, from_account_id):
        self.send_keys(self._amount, amount)
        self.send_keys(self._down_payment, down_payment)
        self.select(self._from_account_id, from_account_id)
        self.click(self._apply_now_button)

    def get_loan_application_result(self):
        return self.get_element_text(self._loan_status)
