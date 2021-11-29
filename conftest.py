import logging

import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

from fixtures.pages.application import Application

logger = logging.getLogger("shop")


def pytest_addoption(parser):
    parser.addoption(
        "--url",
        action="store",
        default="https://berpress.github.io/react-shop",
        help="Shop url",
    ),
    parser.addoption(
        "--username",
        action="store",
        default="super_qa_2021",
        help="username",
    ),
    parser.addoption(
        "--password",
        action="store",
        default="Password11!",
        help="Password",
    ),
    parser.addoption("--headless", action="store_false", help="Headless mode"),


@pytest.fixture()
def app(request):
    url = request.config.getoption("--url")
    headless = request.config.getoption("--headless")

    chrome_options = Options()
    if headless:
        chrome_options.headless = True
    else:
        chrome_options.headless = False
    # chrome_options.headless = False
    chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
    logger.info(f"Start app on {url}")
    app = Application(driver, url)
    yield app
    app.quit()
