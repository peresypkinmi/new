import pytest
from selene.support.shared import browser

from selene.support.shared import browser, config


@pytest.fixture()
def setup_browser_size():
    config.window_width = 1920
    config.window_height = 1080

@pytest.fixture()
def open_base_page(setup_browser_size):
    browser.open('https://google.com')



