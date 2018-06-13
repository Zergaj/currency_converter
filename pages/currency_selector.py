class CurrencySelector:
    def __init__(self, selector):
        self.selector = selector

    button_locator = './/em'
    list_element_locator = './/span[text()="{currency}"]'
    current_element_locator = './/strong'

    def current_element(self):
        return self.selector.find_element_by_xpath(self.current_element_locator)

    def button(self):
        return self.selector.find_element_by_xpath(self.button_locator)

    def list_element(self, value):
        return self.selector.find_element_by_xpath(self.list_element_locator.replace('{currency}', value))
