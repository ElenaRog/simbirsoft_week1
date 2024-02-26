from utils.generator import RandomData
from pages.main_page import MainPage
from pages.add_customer_page import AddCustomerPage
from pages.customers_page import CustomerPage
import allure
import pytest
random_user = RandomData()

RANDOM_POST_CODE = random_user.post_code
RANDOM_FIRST_NAME = random_user.first_name

@allure.feature('XYZ Bank')
@allure.story('UI')
@allure.title('Создание клиента (Add Customer)')
@allure.description('''
    Цель: проверить корректность создания клиента
    
    Шаги:
    1. Открыть главную страницу
    2. Перейти на страницу создания клиента
    3. Заполнить поля и подтвердить создание
    4. Проверить в всплывающем окне, что клиент создан
    5. Перейти на страницу со списком клиентов
    6. Проверить, что пользователь с созданным именем в списке
    
    Постусловия:
    - Удалить созданного клиента
    
    Ожидаемый результат:
    - Клиент создан и отображается в списке на странице клиентов
''')
@pytest.mark.parametrize('post_code, first_name', [(RANDOM_POST_CODE, RANDOM_FIRST_NAME)])
def test_add_customer(post_code, first_name):
    with allure.step('Открыть страницу'):
        main_page = MainPage()
        main_page.open()

    with allure.step('Перейти на страницу создания клиента'):
        main_page.go_to_add_customer_page()
        add_custmer_page = AddCustomerPage()


    with allure.step('Заполнить поля данными и подтвердить создание'):
        add_custmer_page.add_customer(post_code, first_name)


    with allure.step('Проверить в всплывающем окне, что клиент создан'):
        add_custmer_page.accept_alert()

    with allure.step('Перейти на страницу со списком клиентов'):
        add_custmer_page.go_to_customers_page()
        customers_page = CustomerPage()

    with allure.step('Проверить, что пользователь с созданным именем в списке'):
        customers_page.find_name(first_name)

    with allure.step('Удаление пользователя'):
        customers_page.delete_customer(first_name)

@allure.feature('XYZ Bank')
@allure.story('UI')
@allure.title('Сортировка клиентов по имени (First Name)')
@allure.description('''
    Цель: проверить сортировку по именам

    Шаги:
    1. Открыть главную страницу
    2. Перейти на страницу со списком клиентов
    3. Нажать на заголовок "First Name" для включения сортировки
    4. Проверить, что имена отображаются в алфавитном порядке

    Ожидаемый результат:
    - После включения сортировки имена отображаются в алфавитном порядке
''')
def test_name_sorting():
    with allure.step('Открыть главную страницу'):
        main_page = MainPage()
        main_page.open()

    with allure.step('Перейти на страницу со списком клиентов'):
        main_page.go_to_customers_page()
        customers_page = CustomerPage()

    with allure.step('Нажать на заголовок "First Name" для включения сортировки'):
        customers_page.sort_by_first_name()

    with allure.step('Проверить, что имена отображаются в алфавитном порядке'):
        customers_page.check_order()


@allure.feature('XYZ Bank')
@allure.story('UI')
@allure.title('Сортировка клиентов по имени (First Name)')
@allure.description('''
    Цель: проверить сортировку по именам

    Шаги:
    1. Открыть главную страницу
    2. Перейти на страницу со списком клиентов
    3. Найти и удалить нужного пользователя
    4. Проверить, что имена отображаются без удаленного пользователя

    Ожидаемый результат:
    - После удаления пользователя он перестает отображаться в таблице
''')
def test_delete_user():
    with allure.step('Открыть главную страницу'):
        main_page = MainPage()
        main_page.open()

    with allure.step('Перейти на страницу со списком клиентов'):
        main_page.go_to_customers_page()
        customers_page = CustomerPage()

    with allure.step('Найти и удалить нужного пользователя'):
        deleted_customer = customers_page.choose_customer_to_delete()
        customers_page.delete_customer(deleted_customer)

    with allure.step('Проверить, что имена отображаются без удаленного пользователя'):
        customers_page.check_name_not_in_list(deleted_customer)
