from pages.page import Page


class QuotationChangeTable(Page):

    close_button_locator = '//*[@class="rates-table-view-close"]'
    table_locator = '//*[@class="modal-content"]'

    def close_button(self):
        return self.element(self.close_button_locator)

    def is_close_button_visible(self):
        return self.is_element_visible(self.close_button_locator)

    def is_table_visible(self):
        return self.is_element_visible(self.table_locator)

    def is_table_invisible(self):
        return self.is_element_invisible(self.table_locator)
