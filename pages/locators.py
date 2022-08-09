from selenium.webdriver.common.by import By


class LoginPageLocators():
    """The class contains information about how 

    and which element to search for on the login page.
    """

    EMAIL_FIELD = (
        By.XPATH, "/html/body/div/div/div/section/div[2]/div/\
        div/div/form/div[1]/div[1]/div/input")
    PASSWORD_FIELD = (
        By.XPATH, "/html/body/div/div/div/section/div[2]/div/div/\
        div/form/div[1]/div[2]/div/input")
    BUTTON_SUBMIT = (
        By.XPATH, "/html/body/div/div/div/section/div[2]/div/div/\
        div/form/div[2]/button")
    FORGOT_PASSWORD = (
        By.XPATH, "/html/body/div/div/div/section/div[2]/div/\
        div/div/div[2]/a")
    EMAIL_ERROR = (
        By.XPATH, "/html/body/div/div/div/section/div[2]/div/\
        div/div/form/div[1]/div[1]/div/div")
    PASSWORD_ERROR = (
        By.XPATH, "/html/body/div/div/div/section/div[2]/div/div/\
        div/form/div[1]/div[2]/div/div")
    ERROR_MESSAGE = (
        By.XPATH, "/html/body/div/div[2]/div/section/\
        div[2]/div/div/div/form/div[1]")


class PersonalAccountNotConfirmedLocators():
    """
    The class contains information about how 

    and which element to search for on the not confirmed personal account.
    """

    PASSPORT_BUTTON = (By.XPATH,
                       "/html/body/div/div/div/div[3]/div/div/div[3]/\
                       div/div/div[2]/div[2]/div[1]")
    PASSPORT_FORM = (
        By.XPATH, "/html/body/div/div/div/div[3]/\
        div/div/div[3]/div/div/div[2]")
    PASSPORT_FORM_SURNAME = (By.ID, "surname")
    PASSPORT_FORM_NAME = (By.ID, "name")
    PASSPORT_FORM_PATRONYMIC = (By.ID, "patronymic")
    PASSPORT_BIRTHDAY = (By.ID, "birthday")
    PASSPORT_DATEPICKER = (
        By.XPATH, "/html/body/div[1]/div/div/div[3]/\
        div/div/div[3]/div/div/div[2]/div[3]/div[2]/div/div[1]/div/div/input")
    DATEPICKER_CURR_YEAR = (
        By.XPATH, "/html/body/div[2]/div/div/div/div[1]/span/button[2]")
    DATEPICKER_DOUBLE_LEFT = (
        By.XPATH, "/html/body/div[2]/div/div/div/div[1]/button[1]")
    DATEPICKER_LEFT = (
        By.XPATH, "/html/body/div[2]/div/div/div/div[1]/button[2]")
    DATEPICKER_DOUBLE_RIGHT = (
        By.XPATH, "/html/body/div[2]/div/div/div/div[1]/button[3]")
    DATEPICKER_RIGHT = (
        By.XPATH, "/html/body/div[2]/div/div/div/div[1]/button[4]")
    DATEPICKER_CURR_MONTH = (
        By.XPATH, "/html/body/div[2]/div/div/div/div[1]/span/button[1]")
    SERIES_FIELD = (By.ID, "passportSeries")
    NUMBER_FIELD = (By.ID, "passportNumber")
    CODE_FIELD = (By.ID, "code")
    SNILS_FIELD = (By.ID, "cardId")
    DATE_ISSUE_FIELD = (By.ID, "dateOfIssue")
    ISSUED_FIELD = (By.ID, "issued")
    ADDRESS_FIELD = (
        By.XPATH, "/html/body/div/div/div/div[3]/div/div/\
        div[3]/div/div/div[2]/div[3]/div[5]/div/div/div/div/div/input")
    ADDRES_LIST = (By.XPATH,
                   "/html/body/div/div/div/div[3]/div/div/div[3]/div/div/\
                   div[2]/div[3]/div[5]/div/div/div/div/div[2]/span")
    PHONE_FIELD = (By.ID, "phone")
    ATTACH_BUTTON = (
        By.XPATH, "/html/body/div/div/div/div[3]/div/div/div[3]/div/\
        div/div[2]/div[3]/div[9]/button[1]")
    ATTACH_FILE = (
        By.XPATH, "/html/body/div/div/div/div[3]/div/div/div[3]/div/\
        div/div[2]/div[3]/div[8]/input")
    SEND_BUTTON = (
        By.XPATH, "/html/body/div/div/div/div[3]/div/div/div[3]/div/\
        div/div[2]/div[3]/div[9]/button[2]")
    DELETE_FILE = (
        By.XPATH, "/html/body/div/div/div/div[3]/div/div/div[3]/div/\
        div/div[2]/div[3]/div[8]/div/div/img")
    STATUS_PASSPORT_FORM = (By.XPATH,
                            "/html/body/div/div/div/div[3]/div/div/\
                            div[3]/div/div/div[2]/div[2]/div[1]/div[1]")
    DIPLOM_FORM_BUTTON = (
        By.XPATH, "/html/body/div/div/div/div[3]/div/div/\
        div[3]/div/div/div[2]/div[2]/div[2]")
