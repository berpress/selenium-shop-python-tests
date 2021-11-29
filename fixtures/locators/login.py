from selenium.webdriver.common.by import By


class LoginLocators:
    LOGIN_PAGE = (By.ID, "login-link")
    EMAIL_INPUT = (By.ID, "name")
    PASSWORD_INPUT = (By.ID, "password")
    BUTTON_SUBMIT = (By.ID, "register")
