from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, app):
        self.app = app

    def _find_element(self, locator, wait_time=20):
        """
        Find element. Use Explicit wait
        :param locator: locator like (By.ID, 'name')
        :param wait_time: wait time
        :return: return selenium element
        """
        element = WebDriverWait(self.app.driver, wait_time).until(
            EC.presence_of_element_located(locator),
            message=f"Can't find element by locator {locator}",
        )
        return element

    def click(self, locator, wait_time=20):
        """
        Click element
        """
        element = self._find_element(locator, wait_time)
        element.click()

    def fill(self, value: str, locator, wait_time=60):
        """
        Fill element (fill == send_keys)
        :param data: string to fill
        """
        element = self._find_element(locator, wait_time)
        if value:
            element.send_keys(value)

    def text(self, locator, wait_time=20) -> str:
        """
        Get element text
        """
        element = self._find_element(locator, wait_time)
        return element.text
