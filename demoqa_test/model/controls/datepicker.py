from selene.support.shared import browser


def select(selector, month, year, day):
    browser.element(selector).click()
    browser.element('.react-datepicker__month-select').send_keys(month)
    browser.element('.react-datepicker__year-select').send_keys(year)
    browser.element(f'.react-datepicker__day--0{day}').click()