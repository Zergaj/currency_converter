from pages.page import Page
from selenium.webdriver.common.by import By


class PrintPopup(Page):

    opened_print_popup_locator = '//*[@class="details-item print-visible"]'
    closed_print_popup_locator = '//*[@class="details-item print-invisible"]'
    close_button_locator = '//button[text()="Закрыть"]'

    def close_button(self):
        return self.driver.find_element_by_xpath(self.close_button_locator)

    def is_close_button_visible(self):
        return self.is_element_visible((By.XPATH, self.close_button_locator))

    def is_print_popup_visible(self):
        return self.is_element_visible((By.XPATH, self.opened_print_popup_locator))

    def is_print_popup_invisible(self):
        return self.is_element_visible((By.XPATH, self.closed_print_popup_locator))