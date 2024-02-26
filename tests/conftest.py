import pytest

from selene import browser
from utils import attach

@pytest.fixture(scope='function', autouse=True)
def setup_browser(request):
    browser.config.window_height = 1080
    browser.config.window_width = 1920
    browser.config.base_url = 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager'

    yield browser

    attach.add_screenshot(browser)
    attach.add_logs(browser)

    browser.quit()
