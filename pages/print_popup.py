from pages.page import Page


class PrintPopup(Page):

    opened_print_popup_locator = '//*[@class="details-item print-visible"]'
    closed_print_popup_locator = '//*[@class="details-item print-invisible"]'
    close_button_locator = '//button[text()="Закрыть"]'

    def close_button(self):
        return self.element(self.close_button_locator)

    def is_close_button_visible(self):
        return self.is_element_visible(self.close_button_locator)

    def is_print_popup_visible(self):
        return self.is_element_visible(self.opened_print_popup_locator)

    def is_print_popup_invisible(self):
        return self.is_element_visible(self.closed_print_popup_locator)