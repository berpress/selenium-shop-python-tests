import logging

from fixtures.locators.items import MainLocators
from fixtures.locators.register import RegisterLocators
from fixtures.pages.base_page import BasePage

logger = logging.getLogger("moodle")


class ItemsPage(BasePage):
    def add_to_cart(self) -> None:
        """
        Add first item to cart
        """
        logger.info("Try to add item to cart")
        self.click(locator=MainLocators.LOGO)
        self.click(locator=MainLocators.BUY)

    def buy(self) -> None:
        logger.info("Try to buy item from cart")
        self.click(locator=MainLocators.CART)
        self.click(locator=MainLocators.BUY_BUTTON)

    def get_toast_text(self) -> str:
        return self.text(locator=RegisterLocators.TOAST)

    def get_error(self) -> str:
        return self.text(locator=RegisterLocators.ERROR)
