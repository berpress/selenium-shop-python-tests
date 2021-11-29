import logging

from fixtures.locators.login import LoginLocators
from fixtures.locators.register import RegisterLocators
from fixtures.models.register import RegisterData
from fixtures.pages.base_page import BasePage

logger = logging.getLogger("moodle")


class LoginPage(BasePage):
    def auth(self, data: RegisterData) -> None:
        logger.info(
            f"Try to auth with email {data.email}, " f"password {data.password}"
        )
        self.click(locator=LoginLocators.LOGIN_PAGE)
        self.fill(value=data.email, locator=LoginLocators.EMAIL_INPUT)
        self.fill(value=data.password, locator=LoginLocators.PASSWORD_INPUT)
        self.click(locator=LoginLocators.BUTTON_SUBMIT)

    def get_toast_text(self) -> str:
        return self.text(locator=RegisterLocators.TOAST)

    def get_error(self) -> str:
        return self.text(locator=RegisterLocators.ERROR)
