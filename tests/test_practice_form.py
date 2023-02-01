from demoqa_test.model.pages import practice_form


def test_successful_student_registration_form():
    practice_form.open_page()

    practice_form.set_firstname_and_lastname('Dinara', 'Shurukhina')

    practice_form.set_contacts('testEmail@gmail.com', '81234567890', 'Tverskaya str, 19, 173')

    practice_form.set_gender('Female')

    practice_form.set_birthday('May', '1986', '14')

    practice_form.set_subjects('Computer Science')

    practice_form.set_hobby('Reading')

    practice_form.upload_file('photo_2016-08-25_20-45-23.jpg')

    practice_form.scroll_to_state()

    practice_form.choose_state('NCR')
    practice_form.choose_city('Delhi')

    practice_form.submit()

    practice_form.validation(
        'Dinara Shurukhina',
        'testEmail@gmail.com',
        'Female',
        '8123456789',
        '14 May,1986',
        'Computer Science',
        'Reading',
        'photo_2016-08-25_20-45-23.jpg',
        'Tverskaya str, 19, 173',
        'NCR Delhi'
    )
