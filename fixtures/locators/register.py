from selenium.webdriver.common.by import By


class RegisterLocators:
    REGISTER_PAGE = (By.ID, "register-link")
    EMAIL_INPUT = (By.ID, "name")
    PASSWORD_INPUT = (By.ID, "password1")
    PASSWORD_INPUT_2 = (By.ID, "password2")
    REGISTER_BUTTON = (By.ID, "register")
    TOAST = (By.ID, "toast-container")
