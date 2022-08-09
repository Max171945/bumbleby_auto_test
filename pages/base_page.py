from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage():
    """     
    The class of the base page from which all other classes will be inherited.
    """

    def __init__(self, browser, url):
        """ Creating a page object """
        self.browser = browser
        self.url = url

    def open(self):
        """ The method opens the desired page in the browser """
        self.browser.get(self.url)

    def is_element_present(self, how, what, timeout=5):
        """ The method checks for the presence of an element on the page """
        try:
            WebDriverWait(self.browser, timeout).until(
                EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

    def is_not_element_present(self, how, what, timeout=5):
        """ 
        The method checks the absence of an element for a specified time
        """

        return not self.is_element_present(how, what, timeout)

    def is_disappeared(self, how, what, timeout=5):
        """        
        The method checks the disappearance of an element for a certain time
        """
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).\
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

    def is_element_active(self, how, what, timeout=5):
        """ The method checks whether the element is active """

        try:
            WebDriverWait(self.browser, timeout).until(
                EC.element_to_be_clickable((how, what)))
        except TimeoutException:
            return False
        return True
