import pytest
from selenium import webdriver


def pytest_addoption(parser):
    """ Add browser selection option """
    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Choose browser: chrome or firefox")


@pytest.fixture(scope="function")
def browser(request):
    """ Initializing the browser and cleaning after """
    browser_name = request.config.getoption("browser_name").lower()
    browser = None

    if browser_name == "chrome":
        browser = webdriver.Chrome()
    elif browser_name == "firefox":
        browser = webdriver.Firefox()
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")

    browser.maximize_window()

    yield browser
    browser.quit()
