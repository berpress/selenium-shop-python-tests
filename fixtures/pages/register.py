import logging

from fixtures.locators.register import RegisterLocators
from fixtures.models.register import RegisterData
from fixtures.pages.base_page import BasePage

logger = logging.getLogger("moodle")


class RegisterPage(BasePage):
    def register(self, data: RegisterData) -> None:
        logger.info(
            f"Try to register with email {data.email}, "
            f"first password {data.password}, second password {data.password_2}"
        )
        # time.sleep(5)
        self.click(locator=RegisterLocators.REGISTER_PAGE)
        self.fill(value=data.email, locator=RegisterLocators.EMAIL_INPUT)
        self.fill(value=data.password, locator=RegisterLocators.PASSWORD_INPUT)
        self.fill(value=data.password_2, locator=RegisterLocators.PASSWORD_INPUT_2)
        self.click(locator=RegisterLocators.REGISTER_BUTTON)

    def get_toast_text(self) -> str:
        return self.text(locator=RegisterLocators.TOAST)
