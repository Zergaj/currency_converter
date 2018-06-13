from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import *
from selenium.common.exceptions import WebDriverException


class Page:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def is_element_visible(self, locator):
        try:
            return self.wait.until(visibility_of_element_located(locator))
        except WebDriverException:
            return False

    def is_element_invisible(self, locator):
        try:
            return self.wait.until(invisibility_of_element_located(locator))
        except WebDriverException:
            return False

    def open(self, url):
        return self.driver.get(url)

    def scroll_page_down(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def scroll_page_up(self):
        self.driver.execute_script("window.scrollTo(0, 0);")
