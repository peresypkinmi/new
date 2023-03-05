from selene.support.shared import browser
from selene import be, have

def test_searchresult_is_exist(open_base_page):
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))

def test_searchresult_is_no_exist(open_base_page):
    browser.element('[name="q"]').should(be.blank).type('lkjhgjhgjhgjhfchxgfdh').press_enter()
    browser.element('p[role=heading]').should(have.text('ничего не найдено.'))

