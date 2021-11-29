from fixtures.pages.register import RegisterPage


class Application:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url
        self.register = RegisterPage(self)

    def quit(self):
        self.driver.quit()

    def open_main_page(self):
        self.driver.get(self.url)