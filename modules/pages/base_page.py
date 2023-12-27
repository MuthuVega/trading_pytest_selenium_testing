from selenium.webdriver.common.actions.key_actions import KeyActions


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def get_page_title(self):
        title = self.driver.title
        return title

    def do_send_data(self, by_locator, text):
        self.driver.find_element(by_locator[0], by_locator[1]).send_keys(text)

    def is_link_exist(self, by_locator):
        element = self.driver.find_elements(by_locator[0], by_locator[1])
        if element:
            return self.driver.find_element(by_locator[0], by_locator[1]).is_displayed()
        else:
            return False
