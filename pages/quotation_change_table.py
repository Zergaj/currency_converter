from pages.page import Page
from selenium.webdriver.common.by import By


class QuotationChangeTable(Page):

    close_button_locator = '//*[@class="rates-table-view-close"]'
    table_locator = '//*[@class="modal-content"]'

    def close_button(self):
        return self.driver.find_element_by_xpath(self.close_button_locator)

    def is_close_button_visible(self):
        return self.is_element_visible((By.XPATH, self.close_button_locator))

    def is_table_visible(self):
        return self.is_element_visible((By.XPATH, self.table_locator))

    def is_table_invisible(self):
        return self.is_element_invisible((By.XPATH, self.table_locator))
