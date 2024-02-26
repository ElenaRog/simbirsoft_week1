from selene import browser


class BasePage:
    def open(self):
        browser.open('')

    def go_to_customers_page(self):
        browser.open('/list')

    def go_to_add_customer_page(self):
        browser.open('/addCust')

    def clear_input_and_enter_text(self):
        pass
