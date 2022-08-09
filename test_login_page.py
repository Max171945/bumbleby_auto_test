import pytest
from pages.login_page import LoginPage

link = "https://qa.neapro.site/login/"


class TestLoginAuthorization():
	""" The class is testing authorization """

	correct_email = "max171945@yandex.ru"
	correct_password = "11111111"
	uncorrect_password = "2323gsf"
	uncorrect_email = "tes@tes.ru"

	def open_login_page(self, driver):
		page = LoginPage(driver, link)
		page.open()
		return page

	#Test-case ID=C5
	def test_authorization_with_correct_data(self, browser):
		""" Authorization with the correct username and password """
		page = self.open_login_page(browser)
		page.authorization(self.correct_email, self.correct_password)
		page.is_success_authorization(link)		

	#Test-case ID=C8
	def test_authorization_correct_email_uncorrect_pass(self, browser):
		""" Authorization with the correct username and uncorrect password """
		page = self.open_login_page(browser)
		page.authorization(self.correct_email, self.uncorrect_password)
		page.should_be_message_error()

	#Test-case ID=C9
	def test_authorization_uncorrect_email_correct_pass(self, browser):
		""" Authorization with the uncorrect username and correct password """
		page = self.open_login_page(browser)
		page.authorization(self.uncorrect_email, self.correct_password)
		page.should_be_message_error()

class TestLoginFieldValidation():
	""" The class checks the validation of the login field """
	
	valid_email = [
	    'email@email.ru', 'EMAIL@EMAIL.RU', '7ema7il7@email.ru',
	    'email@em78ail.r347u', 'ema-il@email.ru', 'email@em-ail.ru',
	    'em_ail@email.ru', 'email@ema_il.ru', 'e.ma.il@email.ru',
	    'email@em.ai.l.ru'
	]

	invalid_email = [
	    'email@emailru', 'emailemail.ru', 'ema il@email.ru',
	    'email@ema il.ru', '@email.ru', 'email@', '.email@email.ru',
	    'email.@email.ru', 'email@-email.ru', 'email@email-.ru',
	    'ema...il@email.ru', '♣♂', '“”‘~!@#$%^&*()?>,./\<][ /*<!–“”, “${code}”;–>',
	    '           '
	]


	#Test-case ID=C22
	@pytest.mark.parametrize('email', valid_email)
	def test_valid_date_in_email_field(self, browser, email):
		""" The method tests valid data in the login field """

		page = LoginPage(browser, link)
		page.open()
		page.fill_email(email)
		page.should_not_be_email_error()

	#Test-case ID=C23
	@pytest.mark.parametrize('email', invalid_email)
	def test_invalid_date_in_email_field(self, browser, email):
		""" The method tests invalid date in the login field """

		page = LoginPage(browser, link)
		page.open()
		page.fill_email(email)
		page.should_be_email_error()



