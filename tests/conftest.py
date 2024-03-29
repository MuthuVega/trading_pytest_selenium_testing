import pytest

from modules.pages.login_page import LoginPage
from modules.tradingMod import v20_api
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="function", autouse=False)
def v20_user_acc_api_client():
    yield v20_api.UserAccounts()


@pytest.fixture(scope="class", autouse=False)
def init_webdriver(request):
    chrome_options = Options()
    chrome_options.add_argument("-headless")
    web_driver = webdriver.Chrome(options=chrome_options)
    request.cls.driver = web_driver
    yield
    web_driver.close()


@pytest.fixture(scope="function", autouse=False)
def login_page(request):
    yield LoginPage(request.cls.driver)
