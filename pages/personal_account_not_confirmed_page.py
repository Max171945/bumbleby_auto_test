import time
from .base_page import BasePage
from .locators import PersonalAccountNotConfirmedLocators as PANC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

time_sleep = 0.5

# It is necessary to separate work with form fields into a separate class


class PersonalAccountNotConfirmedPage(BasePage):
    """ The class associated with the not confirmed personal account page """

    unloaded_passport = "не загружено"
    loaded_passport = "загружено"
    confirmed_passport = "принято"

    number = {
        "янв.": "01",
        "февр.": "02",
        "март": "03",
        "апр.": "04",
        "май": "05",
        "июнь": "06",
        "июль": "07",
        "авг.": "08",
        "сент.": "09",
        "окт.": "10",
        "нояб": "11",
        "дек.": "12"
    }

    def scroll_to_element(self, element):
        """ The method scrolls to the selected element """

        self.browser.execute_script(
            "return arguments[0].scrollIntoView(true);", element)

    def open_passport_form(self):
        """ The method opens a form with passport data """

        self.should_be_passport_button()
        button = self.browser.find_element(*PANC.PASSPORT_BUTTON)
        button.click()
        assert self.is_element_present(
            *PANC.PASSPORT_FORM), "There is no form with passport data"

    def should_be_passport_button(self):
        """ 
        The method checks for the presence of a button to open a form with passport data
        """

        assert self.is_element_present(*PANC.PASSPORT_BUTTON), \
            "There is no button to open the form with passport data"

    def fill_field(self, text, how, what):
        field = self.browser.find_element(how, what)
        # self.scroll_to_element(field)
        field.clear()
        field.send_keys(text)
        return field

    def fill_last_name_field(self, text):
        """ The method fills in the last name field """

        self.should_be_last_name_field()
        self.fill_field(text, *PANC.PASSPORT_FORM_SURNAME)

    def should_be_last_name_field(self):
        """ The method checks for the presence of a last name field """

        assert self.is_element_present(
            *PANC.PASSPORT_FORM_SURNAME), "There is no last name field"

    def fill_first_name_field(self, text):
        """ The method fills in the first name field """

        self.should_be_first_name_field()
        self.fill_field(text, *PANC.PASSPORT_FORM_NAME)

    def should_be_first_name_field(self):
        """ The method checks for the presence of a first name field """

        assert self.is_element_present(
            *PANC.PASSPORT_FORM_NAME), "There is no first name field"

    def fill_patronymic_field(self, text):
        """ The method fills in the patronymic field """

        self.should_be_patronymic_field()
        self.fill_field(text, *PANC.PASSPORT_FORM_PATRONYMIC)

    def should_be_patronymic_field(self):
        """ The method checks for the presence of a patronymic field """

        assert self.is_element_present(*PANC.PASSPORT_FORM_PATRONYMIC), \
            "There is no patronymic field"

    def fill_date_birth(self, year, month, day):
        """ The method fills in the date of birth """

        self.should_be_date_birth()
        date_birth = self.browser.find_element(*PANC.PASSPORT_BIRTHDAY)
        date_birth.click()
        self.should_datepicker()
        self.set_date_on_datepicker(year, month, day)

    def should_be_date_birth(self):
        """ The method checks for the presence of the date of birth field """

        assert self.is_element_present(*PANC.PASSPORT_BIRTHDAY), \
            "There is no date of birth field"

    def should_datepicker(self):
        """ The method checks for the presence of the datepicker """

        assert self.is_element_present(*PANC.PASSPORT_DATEPICKER), \
            "There is no datepicker"

    def set_date_on_datepicker(self, year, month, day):

        double_left = self.browser.find_element(*PANC.DATEPICKER_DOUBLE_LEFT)
        left = self.browser.find_element(*PANC.DATEPICKER_LEFT)
        double_right = self.browser.find_element(*PANC.DATEPICKER_DOUBLE_RIGHT)
        right = self.browser.find_element(*PANC.DATEPICKER_RIGHT)
        curr_year = self.browser.find_element(*PANC.DATEPICKER_CURR_YEAR)
        curr_month = self.browser.find_element(*PANC.DATEPICKER_CURR_MONTH)

        while curr_year.text != year:
            if int(curr_year.text) < int(year):
                double_right.click()
            else:
                double_left.click()

        while curr_month.text != month:
            left.click()

        date = year + "-" + self.number[month] + "-" + day
        button = self.browser.find_element(By.CSS_SELECTOR,
                                           f"td[title='{date}']")
        button.click()

    def fill_masked_field(self, text, how, what):
        """ The method fills in the fields with masks """

        field = self.browser.find_element(how, what)
        # self.scroll_to_element(field)
        field.clear()
        field.send_keys(Keys.HOME)
        for symbol in text:
            field.send_keys(symbol)
            time.sleep(time_sleep)

    def fill_passport_series(self, text):
        """ The method fills in the series field """

        self.should_be_passport_series_field()
        self.fill_masked_field(text, *PANC.SERIES_FIELD)

    def should_be_passport_series_field(self):
        """ The method checks for the presence of the series field """

        assert self.is_element_present(*PANC.SERIES_FIELD), \
            "There is no series field"

    def fill_passport_number(self, text):
        """ The method fills in the number field """

        self.should_be_passport_number()
        self.fill_masked_field(text, *PANC.NUMBER_FIELD)

    def should_be_passport_number(self):
        """ The method checks for the presence of the number field """

        assert self.is_element_present(*PANC.NUMBER_FIELD), \
            "There is no passport number field"

    def fill_code_field(self, text):
        """ The method fills in the code field """

        self.should_be_code_field()
        self.fill_masked_field(text, *PANC.CODE_FIELD)

    def should_be_code_field(self):
        """ The method checks for the presence of the code field """

        assert self.is_element_present(*PANC.CODE_FIELD), \
            "There is no code field"

    def fill_snils_field(self, text):
        """ The method fills in the snils field """

        self.should_be_snils_field()
        self.fill_masked_field(text, *PANC.SNILS_FIELD)

    def should_be_snils_field(self):
        """ The method checks for the presence of the snils field """

        assert self.is_element_present(*PANC.SNILS_FIELD), \
            "There is no snils field"

    def fill_date_issue_field(self, year, month, day):
        """ The method fills in the issue date field """

        self.should_be_date_issue_field()
        date_issue = self.browser.find_element(*PANC.DATE_ISSUE_FIELD)
        date_issue.click()
        self.should_datepicker()
        self.set_date_on_datepicker(year, month, day)

    def should_be_date_issue_field(self):
        """ The method checks for the presence of the issue date field """

        assert self.is_element_present(*PANC.DATE_ISSUE_FIELD), \
            "There is no date issue field"

    def fill_issued_field(self, text):
        """ The method fills in the by whom field """

        self.should_be_issued_field()
        self.fill_field(text, *PANC.ISSUED_FIELD)

    def should_be_issued_field(self):
        """ The method checks for the presence of the by whom field """

        assert self.is_element_present(*PANC.ISSUED_FIELD), \
            "There is no issued field"

    def fill_address_field(self, text):
        """ The method fills in the address field """

        self.should_be_address_field()
        address = self.browser.find_element(*PANC.ADDRESS_FIELD)
        self.scroll_to_element(address)        
        address.send_keys(Keys.HOME)
        address.send_keys(Keys.CONTROL+"a")
        address.send_keys(Keys.DELETE)

        # Revision needed
        for symbol in text:
            address.send_keys(symbol)

            # implement waiting using webdriver
            time.sleep(time_sleep)
            addrlist = self.browser.find_elements(*PANC.ADDRES_LIST)
            for element in addrlist:
                if text == element.text:
                    self.scroll_to_element(element)
                    element.click()
                    return

    def should_be_address_field(self):
        """ he method checks for the presence of the address field """

        assert self.is_element_present(*PANC.ADDRESS_FIELD), \
            "There is no address field"

    def fill_phone_field(self, text):
        """ The method fills in the phone fields """

        self.should_be_phone_field()
        self.fill_masked_field(text, *PANC.PHONE_FIELD)

    def should_be_phone_field(self):
        """ The method checks for the presence of the phone field """

        assert self.is_element_present(*PANC.PHONE_FIELD), \
            "There is no phone field"

    def attach_passport_file(self, file):
        """ The method attaches a scan of the passport """

        self.should_be_attach_passport_button()
        self.is_attach_passport_button_active()
        button = self.browser.find_element(*PANC.ATTACH_BUTTON)
        self.scroll_to_element(button)
        button.click()
        inputfile = self.browser.find_element(*PANC.ATTACH_FILE)
        inputfile.send_keys(file)

    def should_be_attach_passport_button(self):
        """ 
        The method checks for the presence of the attach passport button
        """

        assert self.is_element_present(*PANC.ATTACH_BUTTON), \
            "There is no attach passport button"

    def is_attach_passport_button_active(self):
        """ 
        The method checks the clickability of the attach passport button
        """

        assert self.is_element_active(*PANC.ATTACH_BUTTON), \
            "The attach passport button is not active"

    def delete_attached_files(self):
        """ The method deletes the attached files """
        files = self.browser.find_elements(*PANC.DELETE_FILE)
        for file in files:
            self.scroll_to_element(file)
            file.click()
            self.is_not_element_present(*PANC.DELETE_FILE)

    def click_to_send_passport_data_button(self):
        """ Method click on the send button """

        self.should_be_send_passport_button()
        self.is_send_passport_data_button_active()
        button = self.browser.find_element(*PANC.SEND_BUTTON)
        self.scroll_to_element(button)
        button.click()

    def should_be_send_passport_button(self):
        """ The method checks for the presence of the send passport button """

        assert self.is_element_present(*PANC.SEND_BUTTON), \
            "There is no send passport data button"

    def is_send_passport_data_button_active(self):
        """ 
        The method checks the clickability of the send passport data button
        """

        assert self.is_element_active(*PANC.SEND_BUTTON), \
            "The send passport button is not active"

    def is_status_passport_button_loaded(self):
        """
        The method checks that the status of the passport data button is loaded
        """

        self.should_be_passport_button()
        status = self.browser.find_element(*PANC.STATUS_PASSPORT_FORM).text
        assert status == self.loaded_passport, \
            f"Status - {status}, but should be {self.loaded_passport}"

    def is_diploma_form_button_active(self):
        """ Checks whether the diploma upload form button is active """

        self.should_be_diploma_form_button()
        assert self.is_element_active(*PANC.DIPLOM_FORM_BUTTON), \
            "The diploma upload form button is not active but should be"

    def should_be_diploma_form_button(self):
        """
        The method checks for the presence of the diploma upload form button
        """

        assert self.is_element_present(*PANC.DIPLOM_FORM_BUTTON), \
            "There is no diploma upload form button"
