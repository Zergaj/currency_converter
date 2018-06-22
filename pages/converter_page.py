from pages.page import Page


class ConverterPage(Page):

    header_locator = '//*[@class="header_widget"]'
    cookie_panel_close_button_locator = '//*[@class="cookie-warning__close"]'

    rates_filter_header_locator = '//h6[text()="Конвертация"]'
    show_button_locator = '//*[@class="rates-button"]'
    rates_result_block_locator = '//*[@class="rates-converter-result"]'
    rates_result_to_locator = \
        '//*[@class="rates-converter-result"]/descendant::span[@class="rates-converter-result__total-to"]'
    print_link_locator = '//span[text()="Распечатать"]'
    quotation_change_table_link_locator = '//span[text()="Таблица изменения котировок"]'

    amount_field_locator = '//input[@placeholder="Сумма"]'

    cur_from_locator = \
        '//*[@class="rates-aside__filter-block-line rates-aside__filter-block-line_field_converter-from"]' \
        '/child::div[@class="rates-aside__filter-block-line-right"]'
    cur_to_locator = \
        '//div[@class="rates-aside__filter-block-line"][2]' \
        '/child::div[@class="rates-aside__filter-block-line-right"]'

    source = {
        'card': '//div[text()="Карта Сбербанка"]/parent::label',
        'account': '//div[text()="Счет в Сбербанке"]/parent::label',
        'cash': '//div[text()="Наличные"]/parent::label'
    }
    receiving = {
        'to_card': '//div[text()="На карту Сбербанка"]/parent::label',
        'to_account': '//div[text()="На счет в Сбербанке"]/parent::label',
        'cash': '//div[text()="Выдать наличные"]/parent::label',
        'cashless': '//div[text()="Безналичная оплата услуг/товаров"]/parent::label'
    }
    exch_way = {
        'internet_bank': '//div[text()="Интернет-банк"]/parent::label',
        'branch_bank': '//div[text()="Отделение (ВСП)"]/parent::label',
        'atm': '//div[text()="Банкомат / УС"]/parent::label'
    }
    package = {
        'no_package': '//div[text()="Нет пакета"]/parent::label',
        'primary': '//div[text()="Премьер"]/parent::label',
        'sber_first': '//div[text()="Сбербанк Первый"]/parent::label',
        'private_banking': '//div[text()="Private Banking"]/parent::label'
    }
    date_selector = {
        'current': '//div[text()="Текущее"]/parent::label',
        'selected': '//div[text()="Выбрать"]/parent::label'
    }

    converter_datepicker_locator = '//*[@data-property="converterDate"]'
    converter_datepicker_button_locator = '//input[@data-property="converterDate"]/following-sibling::button'

    datepicker_popup_locator = '//*[@id="ui-datepicker-div"]'
    yerapicker_list_locator = '//*[@id="select2-drop"]'
    yearpicker_item_locator = '//*[@id="select2-drop"]/descendant::div[text()="{year}"]'

    def is_filter_header_visible(self):
        return self.is_element_visible(self.rates_filter_header_locator)

    def is_cookie_panel_close_button_visible(self):
        return self.is_element_visible(self.cookie_panel_close_button_locator)

    def is_cookie_panel_close_button_invisible(self):
        return self.is_element_invisible(self.cookie_panel_close_button_locator)

    def cookie_panel_close_button(self):
        return self.element(self.cookie_panel_close_button_locator)

    def show_button(self):
        return self.element(self.show_button_locator)

    def is_show_button_visible(self):
        return self.is_element_visible(self.show_button_locator)

    def is_rates_result_block_visible(self):
        return self.is_element_visible(self.rates_result_block_locator)

    def rates_result_to(self):
        return self.element(self.rates_result_to_locator)

    def print_link(self):
        return self.element(self.print_link_locator)

    def is_print_link_visible(self):
        return self.is_element_visible(self.print_link_locator)

    def quotation_popup_open_link(self):
        return self.element(self.quotation_change_table_link_locator)

    def is_quotation_popup_open_link_visible(self):
        return self.is_element_visible(self.quotation_change_table_link_locator)

    def amount_field(self):
        return self.element(self.amount_field_locator)

    def is_amount_field_visible(self):
        return self.is_element_visible(self.amount_field_locator)

    # CURRENCY SELECTORS block
    def is_currency_from_visible(self):
        return self.is_element_visible(self.cur_from_locator)

    def currency_from(self):
        return self.element(self.cur_from_locator)

    def is_currency_to_visible(self):
        return self.is_element_visible(self.cur_to_locator)

    def currency_to(self):
        return self.element(self.cur_to_locator)

    # FILTERS
    def source_radio(self, value):
        return self.element(self.source[value])

    def is_source_block_visible(self):
        for i in self.source.values():
            if not self.is_element_visible(i):
                return False
        return True

    def receiving_radio(self, value):
        return self.element(self.receiving[value])

    def is_receiving_block_visible(self):
        for i in self.receiving.values():
            if not self.is_element_visible(i):
                return False
        return True

    def exchange_way_radio(self, value):
        return self.element(self.exch_way[value])

    def is_exchange_way_block_visible(self):
        for i in self.exch_way.values():
            if not self.is_element_visible(i):
                return False
        return True

    def package_radio(self, value):
        return self.element(self.package[value])

    def is_package_block_visible(self):
        for i in self.package.values():
            if not self.is_element_visible(i):
                return False
        return True

    # DATE SELECTORS BLOCK
    def date_radio(self, value):
        if value != 'current':
            value = 'selected'
        return self.element(self.date_selector[value])

    def is_date_block_visible(self):
        for i in self.date_selector.values():
            if not self.is_element_visible(i):
                return False
        return True

    def is_converter_datepicker_visible(self):
        return self.is_element_visible(self.converter_datepicker_locator)

    def converter_datepicker(self):
        return self.element(self.converter_datepicker_locator)

    def converter_datepicker_button(self):
        return self.element(self.converter_datepicker_button_locator)

    def is_datepicker_visible(self):
        return self.is_element_visible(self.datepicker_popup_locator)

    def datepicker(self):
        return self.element(self.datepicker_popup_locator)

    def yearpicker(self):
        return self.element(self.yerapicker_list_locator)

    def is_yearpicker_list_visible(self):
        return self.is_element_visible(self.yerapicker_list_locator)

    def yearpicker_item(self, value):
        return self.element(self.yearpicker_item_locator.replace('{year}', value))
