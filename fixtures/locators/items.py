from selenium.webdriver.common.by import By


class MainLocators:
    BUY = (By.CSS_SELECTOR, '[data-test="buy"]')
    CART = (By.CSS_SELECTOR, ".cart")
    BUY_BUTTON = (By.CSS_SELECTOR, '[data-test="buy-btn"]')
    LOGO = (By.CSS_SELECTOR, ".brand-logo")
