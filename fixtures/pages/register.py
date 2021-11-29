import logging
import time

from fixtures.locators.register import RegisterLocators
from fixtures.models.register import RegisterData
from fixtures.pages.base_page import BasePage

logger = logging.getLogger("moodle")


class RegisterPage(BasePage):
    def register(self, data: RegisterData):
        logger.info(
            f"Try to register with email {data.email}, "
            f"first password {data.password}, second password {data.password_2}"
        )
        time.sleep(5)
        self.click(locator=RegisterLocators.REGISTER_PAGE)
