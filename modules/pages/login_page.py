import time

import pytest
from selenium.webdriver.common.by import By
from modules.pages.base_page import BasePage


class LoginPage(BasePage):
    LOGIN_PAGE = "https://hub.oanda.com"
    USER_NAME = "puttu.hcl@gmail.com"
    PASSWORD = "Meenakshi@123"

    field_user_name = (By.ID, "username")
    field_password = (By.ID, "password")
    button_login = (By.NAME, "action")
    linktext_forgot_password = (By.LINK_TEXT, "Forgot Password?")
    linktext_get_started = (By.LINK_TEXT, "Get Started")
    linktext_login_help = (By.LINK_TEXT, "Login Help")
    linktext_contact_us = (By.LINK_TEXT, "Contact Us")

    def __init__(self, driver):
        super(LoginPage, self).__init__(driver=driver)
        self.driver.get(self.LOGIN_PAGE)
        driver.implicitly_wait(10)

    def login_page_title(self):
        title = self.get_page_title()
        return title

    def login_page_login(self, user_name, password):
        self.do_send_data(self.field_user_name, user_name)
        self.do_send_data(self.field_password, password)
