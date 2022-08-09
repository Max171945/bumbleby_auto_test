import time
from .base_page import BasePage
from .locators import LoginPageLocators

# Revision needed


class LoginPage(BasePage):
    """ The class associated with the login page """

    def authorization(self, email, password):
        """ The method performs authorization and returns the current page """
        self.should_be_email_field()
        self.should_be_password_field()
        self.should_be_submit_button()
        self.fill_email(email)
        self.fill_password(password)
        button = self.browser.find_element(*LoginPageLocators.BUTTON_SUBMIT)
        button.click()
        time.sleep(5)

    def is_success_authorization(self, url):
        """ The method checks the success of authorization """
        assert url != self.browser.current_url, \
            "The personal account page is not open"

    def should_be_email_field(self):
        """ The method checks for the presence of the email field """

        assert self.is_element_present(*LoginPageLocators.EMAIL_FIELD), \
            "There is no email field"

    def should_be_password_field(self):
        """ The method checks for the presence of the password field """

        assert self.is_element_present(*LoginPageLocators.PASSWORD_FIELD), \
            "There is no password field"

    def should_be_submit_button(self):
        """ The method checks for the presence of the submit button """

        assert self.is_element_present(*LoginPageLocators.BUTTON_SUBMIT), \
            "There is no submit button"

    def should_be_ref_forgot_password(self):
        """ The method checks for the presence of the link forgot password """

        assert self.is_element_present(*LoginPageLocators.FORGOT_PASSWORD), \
            "There is no link forgot password"

    def fill_email(self, email):
        """ The method fills in the email field """

        login = self.browser.find_element(*LoginPageLocators.EMAIL_FIELD)
        login.send_keys(email)

    def fill_password(self, password):
        """ The method fills in the password field """

        pass_field = self.browser.find_element(
            *LoginPageLocators.PASSWORD_FIELD)
        pass_field.send_keys(password)

    def should_be_email_error(self):
        """
        The method checks for an error message when validating the email field
        """

        assert self.is_element_present(*LoginPageLocators.EMAIL_ERROR), \
            "There is no an error message when validating the email field"

    def should_be_pass_error(self):
        """
        The method checks for an error message when validating the password field
        """

        assert self.is_element_present(*LoginPageLocators.PASSWORD_ERROR), \
            "There is no an error message when validating the password field"

    def should_be_message_error(self):
        """ The method checks for an error message """

        assert self.is_element_present(*LoginPageLocators.ERROR_MESSAGE), \
            "There is no an error message"

    def should_not_be_email_error(self):
        """
        The method checks for the absence of an error message when validating the email field
        """

        assert self.is_not_element_present(*LoginPageLocators.EMAIL_ERROR), \
            "There is an error message when validating the email field"

    def should_not_be_pass_error(self):
        """
        The method checks for the absence of an error message when validating the password field
        """

        assert self.is_not_element_present(*LoginPageLocators.PASSWORD_ERROR), \
            "There is an error message when validating the password field"

    def should_disappeared_message_error(self):
        """ The method checks for the disappearance of the error message """

        assert self.is_disappeared(*LoginPageLocators.ERROR_MESSAGE), \
            "There is no an error message"
