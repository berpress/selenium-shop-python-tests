import logging

import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

from fixtures.models.register import RegisterData
from fixtures.pages.application import Application

logger = logging.getLogger("shop")


def pytest_addoption(parser):
    parser.addoption(
        "--url",
        action="store",
        default="https://berpress.github.io/react-shop",
        help="Shop url",
    ),
    parser.addoption("--headless", action="store_true", help="Headless mode"),


@pytest.fixture()
def app(request):
    url = request.config.getoption("--url")
    headless = request.config.getoption("--headless")
    chrome_options = Options()
    if headless:
        chrome_options.headless = True
    else:
        chrome_options.headless = False
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
    driver.set_window_size(1920, 1080)
    logger.info(f"Start app on {url}")
    app = Application(driver, url)
    yield app
    app.quit()


@pytest.fixture
def login(app):
    """
    Login fixture
    """
    app.open_main_page()
    data = RegisterData.random()
    app.register.register(data=data)
    app.login.auth(data)


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call" and rep.failed:
        try:
            if "app" in item.fixturenames:
                web_driver = item.funcargs["app"]
            else:
                logger.error("Fail to take screen-shot")
                return
            logger.info("Screen-shot done")
            web_driver.driver.save_screenshot("bag.png")
        except Exception as e:
            logger.error("Fail to take screen-shot: {}".format(e))
