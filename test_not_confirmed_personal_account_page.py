import os
import time
import pytest
from pages.login_page import LoginPage
from pages.personal_account_not_confirmed_page import PersonalAccountNotConfirmedPage


current_dir = os.path.abspath(os.path.dirname(__file__))
test_data = os.path.join(current_dir, 'testing_data')
link = "https://qa.neapro.site/login/"


class TestAddDocumentsPersonalAccountNotConfirmed():
    """
    Checking the addition of documents to the unconfirmed personal account
    """

    # It is necessary to create a separate user class
    # and put personal data there
    email = "max171945@yandex.ru"
    password = "11111111"
    last_name = "Енотиков"
    first_name = "Енотик"
    patronymic = "Енотикович"
    year_birth = "2000"
    month_birth = "май"
    day_birth = "17"
    pass_series = "1111"
    pass_number = "232323"
    issue_year = "2022"
    issue_month = "апр."
    issue_day = "15"
    code = "232355"
    snils = "89775673794"
    issued = "ОВД Енотиковский"
    address = "г Москва, 3-й Дорогобужский пер, д 6 стр 3"
    phone = "7777777777"
    file_one_byte = os.path.join(test_data, 'one.jpeg')
    file_null = os.path.join(test_data, 'nullll.jpeg')

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        """ The method opens the authorization page and authorizes the user """

        self.browser = browser
        page = LoginPage(browser, link)
        page.open()
        page.authorization(self.email, self.password)
        page.is_success_authorization(link)

    # Happy pass
    #Test-case ID=C50
    def test_sending_passport_data(self):
        """ The method checks the sending of passport data """

        page = PersonalAccountNotConfirmedPage(
            self.browser, self.browser.current_url)
        page.open_passport_form()
        page.fill_last_name_field(self.last_name)
        page.fill_first_name_field(self.first_name)
        page.fill_patronymic_field(self.patronymic)
        page.fill_date_birth(self.year_birth, self.month_birth, self.day_birth)
        page.fill_passport_series(self.pass_series)
        page.fill_passport_number(self.pass_number)
        page.fill_date_issue_field(
            self.issue_year, self.issue_month, self.issue_day)
        page.fill_code_field(self.code)
        page.fill_snils_field(self.snils)
        page.fill_issued_field(self.issued)
        page.fill_address_field(self.address)
        page.fill_phone_field(self.phone)
        page.delete_attached_files()
        page.attach_passport_file(self.file_one_byte)
        page.attach_passport_file(self.file_null)
        time.sleep(3)
        page.click_to_send_passport_data_button()
        time.sleep(3)
        page.is_status_passport_button_loaded()
        page.is_diploma_form_button_active()
