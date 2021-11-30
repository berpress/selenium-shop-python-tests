import logging

from fixtures.locators.balance import BalanceLocators
from fixtures.locators.register import RegisterLocators
from fixtures.models.balance import BalanceData
from fixtures.pages.base_page import BasePage

logger = logging.getLogger("moodle")


class BalancePage(BasePage):
    def update_balance(self, data: BalanceData) -> None:
        logger.info(f"Try to update balance user {data.name}, to balance {data.money}")
        self.click(locator=BalanceLocators.BALANCE_PAGE)
        self.fill(value=data.name, locator=BalanceLocators.NAME_INPUT)
        self.fill(value=data.card_number, locator=BalanceLocators.CARD_INPUT)
        self.fill(value=data.date_card, locator=BalanceLocators.CARD_DATE_INPUT)
        self.fill(value=data.money, locator=BalanceLocators.MONEY)
        self.click(locator=BalanceLocators.AGREE_CHECKBOX)
        self.click(locator=BalanceLocators.BUTTON_SUBMIT)

    def get_toast_text(self) -> str:
        return self.text(locator=RegisterLocators.TOAST)

    def get_error(self) -> str:
        return self.text(locator=RegisterLocators.ERROR)
