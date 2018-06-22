from pages.converter_page import ConverterPage
from pages.currency_selector import CurrencySelector
from pages.print_popup import PrintPopup
from pages.quotation_change_table import QuotationChangeTable
from pages.datepicker import Datepicker

import re
import allure


class Application(object):
    def __init__(self, driver, base_url):
        self.driver = driver
        self.base_url = base_url
        self.converter_page = ConverterPage(driver)
        self.print_popup = PrintPopup(driver)
        self.quotation_change_table = QuotationChangeTable(driver)
        self.datepicker = Datepicker
        self.currency_selector = CurrencySelector

    @allure.step('Open converter page http://www.sberbank.ru/ru/quotes/converter')
    def open_converter_page(self):
        self.converter_page.open(self.base_url)

    @allure.step('Converter page has been loaded successfully')
    def is_converter_page_loaded(self):
        return self.converter_page.is_filter_header_visible()

    @allure.step('Close rules panel on screen bottom if it appeared')
    def close_rules_panel(self):
        if self.converter_page.is_cookie_panel_close_button_visible():
            self.converter_page.cookie_panel_close_button().click()
            if self.converter_page.is_cookie_panel_close_button_invisible():
                return

    @allure.step('Press show button')
    def press_show_button(self):
        self.converter_page.scroll_page_down()
        if self.converter_page.is_show_button_visible():
            self.converter_page.show_button().click()

    @allure.step('Result block has appeared')
    def is_result_block_appeared(self):
        return self.converter_page.is_rates_result_block_visible()

    @allure.step('Press print link trying to open print popup')
    def press_print_link(self):
        if self.converter_page.is_print_link_visible():
            self.converter_page.print_link().click()

    @allure.step('Print popup has opened')
    def is_print_popup_opened(self):
        return self.print_popup.is_print_popup_visible()

    @allure.step('Press quotation popup link trying to open quotation popup')
    def press_quotation_popup_link(self):
        if self.converter_page.is_quotation_popup_open_link_visible():
            self.converter_page.quotation_popup_open_link().click()

    @allure.step('Quotation popup has opened')
    def is_quotation_popup_opened(self):
        return self.quotation_change_table.is_table_visible()

    @allure.step('Quotation popup has closed')
    def is_quotation_popup_closed(self):
        return self.quotation_change_table.is_table_invisible()

    @allure.step('Close print popup')
    def close_print_popup(self):
        if self.print_popup.is_close_button_visible():
            self.print_popup.close_button().click()

    @allure.step('Print popup has closed')
    def is_print_popup_closed(self):
        return self.print_popup.is_print_popup_invisible()

    @allure.step('Close quotation popup')
    def close_quotation_popup(self):
        if self.quotation_change_table.is_close_button_visible():
            self.quotation_change_table.close_button().click()

    @allure.step('Check that the default values are set')
    def is_default_data_set(self, data):
        if self.is_current_amount(data[0]) and \
           self.is_selected_currency_from(data[1]) and \
           self.is_selected_currency_to(data[2]) and \
           self.is_selected_source(data[3]) and \
           self.is_selected_receiving(data[4]) and \
           self.is_selected_exchange_way(data[5]) and \
           self.is_selected_pack_service(data[6]) and \
           self.is_selected_converter_date(data[7]):
            return True
        return False

    @allure.step('Enter Amount value: {0}')
    def enter_amount_value(self, value):
        if self.converter_page.is_amount_field_visible():
            self.converter_page.amount_field().clear()
            self.converter_page.amount_field().send_keys(value)

    @allure.step('Assert: displayed Amount should be {0}')
    def is_current_amount(self, value):
        return self.converter_page.amount_field().get_attribute('value') == value

    @allure.step('Select Currency to convert from: {0}')
    def select_currency_from(self, value):
        if self.converter_page.is_currency_from_visible():
            currency_from = self.currency_selector(self.converter_page.currency_from())
            if currency_from.current_element().text != value:
                currency_from.button().click()
                currency_from.list_element(value).click()

    @allure.step('Assert: selected Currency to convert from should be {0}')
    def is_selected_currency_from(self, value):
        return self.currency_selector(self.converter_page.currency_from()).current_element().text == value

    @allure.step('Select Currency to convert to: {0}')
    def select_currency_to(self, value):
        if self.converter_page.is_currency_to_visible():
            currency_to = self.currency_selector(self.converter_page.currency_to())
            if currency_to.current_element().text != value:
                currency_to.button().click()
                currency_to.list_element(value).click()

    @allure.step('Assert: selected Currency to convert to should be {0}')
    def is_selected_currency_to(self, value):
        return self.currency_selector(self.converter_page.currency_to()).current_element().text == value

    @allure.step('Select Source type: {0}')
    def select_source(self, value):
        if self.converter_page.is_source_block_visible():
            if not self.converter_page.source_radio(value).get_attribute('aria-checked'):
                self.converter_page.source_radio(value).click()

    @allure.step('Assert: selected Source type should be {0}')
    def is_selected_source(self, value):
        return self.converter_page.source_radio(value).get_attribute('aria-checked')

    @allure.step('Select Receiving type: {0}')
    def select_receiving(self, value):
        if self.converter_page.is_receiving_block_visible():
            if not self.converter_page.receiving_radio(value).get_attribute('aria-checked'):
                self.converter_page.receiving_radio(value).click()

    @allure.step('Assert: selected Receiving type should be {0}')
    def is_selected_receiving(self, value):
        return self.converter_page.receiving_radio(value).get_attribute('aria-checked')

    @allure.step('Assert: Receiving type {0} should be inactive')
    def is_receiving_inactive(self, value):
        return self.converter_page.receiving_radio(value).get_attribute('aria-disabled')

    @allure.step('Select Exchange way: {0}')
    def select_exchange_way(self, value):
        if self.converter_page.is_exchange_way_block_visible():
            if not self.converter_page.exchange_way_radio(value).get_attribute('aria-checked'):
                self.converter_page.exchange_way_radio(value).click()

    @allure.step('Assert: selected Exchange way should be {0}')
    def is_selected_exchange_way(self, value):
        return self.converter_page.exchange_way_radio(value).get_attribute('aria-checked')

    @allure.step('Assert: Exchange way {0} should be inactive')
    def is_exchange_way_inactive(self, value):
        return self.converter_page.exchange_way_radio(value).get_attribute('aria-disabled')

    @allure.step('Select Package service: {0}')
    def select_pack_service(self, value):
        if self.converter_page.is_package_block_visible():
            if not self.converter_page.package_radio(value).get_attribute('aria-checked'):
                self.converter_page.package_radio(value).click()

    @allure.step('Assert: selected Package service should be {0}')
    def is_selected_pack_service(self, value):
        return self.converter_page.package_radio(value).get_attribute('aria-checked')

    @allure.step('Select Converter Date: {0}')
    def select_converter_date(self, value):
        if self.converter_page.is_date_block_visible():
            if not self.converter_page.date_radio(value).get_attribute('aria-checked'):
                self.converter_page.date_radio(value).click()
            if value != 'current':  # select date
                day, month, year, hour, minute = re.split(r'[.:\s]\s*', value)
                if self.converter_page.is_converter_datepicker_visible() \
                        and self.converter_page.converter_datepicker().get_attribute('value') != value:
                    self.converter_page.converter_datepicker_button().click()
                    if self.converter_page.is_datepicker_visible():
                        datepicker = self.datepicker(self.converter_page.datepicker())
                        self.select_date(datepicker, year=year, month=month, day=day, hour=hour, minute=minute)

    @allure.step('Assert: selected Converter Date should be {0}')
    def is_selected_converter_date(self, value):
        return self.converter_page.date_radio(value).get_attribute('aria-checked')

    @allure.step('Assert: result of convertion should be {0}')
    def check_result(self, value):
        return self.converter_page.rates_result_to().text == value.replace('.', ',')

    def select_date(self, obj, year=None, month=None, day=None, hour=None, minute=None):
        # select year
        if year and obj.is_year_selector_visible() and obj.year_selector().text != year:
            obj.year_selector().click()
            if self.converter_page.is_yearpicker_list_visible():
                self.converter_page.yearpicker_item(year).click()
        # select month
        if month and obj.is_selected_month_visible():
            selected_month = obj.get_month_position(obj.selected_month().text)
            if selected_month != int(month):
                while selected_month != int(month):
                    if selected_month > int(month):
                        obj.month_prev_button().click()
                        selected_month -= 1
                    else:
                        obj.month_next_button().click()
                        selected_month += 1
        # select day
        if day and obj.is_calender_visible():
            obj.day_button(str(int(day))).click()
        # select hour
        if hour and obj.is_hour_selector_visible():
            obj.hour_selector().select_by_visible_text(hour)
        # select minute
        if minute and obj.is_minute_selector_visible():
            obj.minute_selector().select_by_visible_text(minute)
        if obj.is_select_button_visible():
            obj.select_button().click()
