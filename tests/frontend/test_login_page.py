import pytest
from selenium.webdriver.common.by import By

from modules.pages.login_page import LoginPage


@pytest.mark.usefixtures("init_webdriver")
@pytest.mark.muthu
class TestLoginPage:
    def test_login_page_title(self):
        self.login_page = LoginPage(self.driver)
        title = self.login_page.login_page_title()
        print(f"Page title is {title}")

    def test_login_page_login_invalid_user_id(self):
        self.login_page = LoginPage(self.driver)
        self.login_page.login_page_login("testing@dojo.com", "testadmin123")

    def test_check_if_link_is_available(self):
        self.login_page = LoginPage(self.driver)
        assert self.login_page.is_link_exist(LoginPage.linktext_contact_us)
        assert not self.login_page.is_link_exist((By.LINK_TEXT, "muthu"))
