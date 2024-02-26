from .base_page import BasePage

from selene import browser, have, be
from selene.core import query


class CustomerPage(BasePage):
    def sort_by_first_name(self):
        browser.all('tr td a').first.click()

    def get_name_list(self) -> list:
        browser.element('table.table-striped').should(be.visible)
        name_elements = browser.all("//tbody/tr/td[1]")
        names = [element.get(query.text) for element in name_elements]
        return names

    def delete_customer(self, name: str):
        browser.all('tr.ng-scope').element_by(have.text(f'{name}')).element('td button').click()

    def choose_customer_to_delete(self) -> str:
        names = self.get_name_list()
        name_lengths = [len(name) for name in names]
        average_length = sum(name_lengths) / len(name_lengths)
        return min(names, key=lambda x: abs(len(x) - average_length))

    def find_name(self, name: str):
        names = self.get_name_list()
        assert name in names, f'Имя "{name}" не найдено в таблице'

    def check_name_not_in_list(self, name: str):
        names = self.get_name_list()
        assert name not in names, f'Имя "{name}" существует в таблице'

    def check_order(self):
        names_list = self.get_name_list()
        assert ((names_list == sorted(names_list)) or (names_list == sorted(names_list, reverse=True))), \
            'Таблица не отсортирована по именам'
