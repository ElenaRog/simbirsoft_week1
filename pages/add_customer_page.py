from .base_page import BasePage

from selene import browser
from selene.core.entity import Element


class AddCustomerPage(BasePage):
    def input_first_name(self) -> Element:
        return browser.element('[ng-model="fName"][placeholder="First Name"]')

    def input_last_name(self) -> Element:
        return browser.element('[ng-model="lName"][placeholder="Last Name"]')

    def input_post_code(self) -> Element:
        return browser.element('[ng-model="postCd"][placeholder="Post Code"]')

    def submit_button(self) -> Element:
        return browser.element('button.btn-default')

    def add_customer(self, post_code, first_name):
        self.input_first_name().type(first_name)
        self.input_last_name().type(first_name[::-1].title())
        self.input_post_code().type(post_code)
        self.submit_button().click()

    def accept_alert(self):
        al = browser.switch_to.alert
        assert 'Customer added successfully with customer id' in al.text
        al.accept()
