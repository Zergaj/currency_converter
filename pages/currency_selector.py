from pages.page import Page


class CurrencySelector(Page):
    def __init__(self, selector):
        super().__init__(selector)
        self.selector = selector

    button_locator = './/em'
    list_element_locator = './/span[text()="{currency}"]'
    current_element_locator = './/strong'

    def current_element(self):
        return self.element(self.current_element_locator)

    def button(self):
        return self.element(self.button_locator)

    def list_element(self, value):
        return self.element(self.list_element_locator.replace('{currency}', value))
