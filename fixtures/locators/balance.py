from selenium.webdriver.common.by import By


class BalanceLocators:
    BALANCE_PAGE = (By.ID, "blance-link")
    NAME_INPUT = (By.ID, "name")
    CARD_INPUT = (By.ID, "card")
    CARD_DATE_INPUT = (By.ID, "data-card")
    MONEY = (By.ID, "data-money")
    AGREE_CHECKBOX = (By.ID, "agree")
    BUTTON_SUBMIT = (By.CLASS_NAME, "waves-effect")
