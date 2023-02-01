from selene.support.shared import browser
from selene import have


def set_option(selector, text):
    browser.element(selector).click()
    browser.all('[id^=react-select][id*=option]').element_by(have.exact_text(text)).click()
