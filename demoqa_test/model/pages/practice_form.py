from selene.support.shared import browser
from selene import have, be
from demoqa_test.model.controls import radiobutton, datepicker, dropdown, checkbox
from demoqa_test.utils import path_to_file,  scroll


def open_page():
    browser.open('/automation-practice-form')


def set_firstname_and_lastname(firstname, lastname):
    browser.element('#firstName').type(firstname)
    browser.element('#lastName').type(lastname)


def set_contacts(email, phone, address):
    browser.element('#userEmail').type(email)
    browser.element('#userNumber').should(be.blank).type(phone)
    browser.element('#currentAddress').type(address)


def set_gender(value):
    browser.all('[name=gender]').element_by(have.value(value)).element('..').click()
    radiobutton.gender('[name=gender]', value)


def set_birthday(month, year, day):
    datepicker.select('#dateOfBirthInput', month, year, day)


def set_subjects(value):
    browser.element('#subjectsInput').type(value).press_enter()


def set_hobby(value):
    checkbox.hobby('[for^="hobbies-checkbox"]', value)


def upload_file(file_name):
    file_path = path_to_file.get_path(file_name)
    browser.element('#uploadPicture').send_keys(file_path)


def scroll_to_state():
    scroll.scroll_to('#state')


def choose_state(value):
    dropdown.set_option('#state', value)


def choose_city(value):
    dropdown.set_option('#city', value)


def submit():
    browser.element('#submit').click()


def validation(*args):
    browser.element('.table').all('td').even.should(have.texts(args))