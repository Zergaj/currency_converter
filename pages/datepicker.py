from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from pages.page import Page


class Datepicker(Page):
    def __init__(self, datepicker):
        super().__init__(datepicker)
        self.datepicker = datepicker

    months = [
        'Январь',
        'Февраль',
        'Март',
        'Апрель',
        'Май',
        'Июнь',
        'Июль',
        'Август',
        'Сентябрь',
        'Октябрь',
        'Ноябрь',
        'Декабрь'
    ]

    year_selector_locator = './/a[@class="select2-choice"]'
    selected_month_locator = './/*[@class="ui-datepicker-month"]'
    month_prev_button_locator = './/*[@data-handler="prev"]'
    month_next_button_locator = './/*[@data-handler="next"]'
    calender_locator = './/*[@class="ui-datepicker-calendar"]'
    day_button_locator = './/*[text()="{day}"]'

    hour_selector_locator = './/*[@data-unit="hour"]'
    minute_selector_locator = './/*[@data-unit="minute"]'

    select_button_locator = './/*[text()="Выбрать"]'

    def is_year_selector_visible(self):
        return self.is_element_visible((By.XPATH, self.year_selector_locator))

    def year_selector(self):
        return self.datepicker.find_element_by_xpath(self.year_selector_locator)

    def is_selected_month_visible(self):
        return self.is_element_visible((By.XPATH, self.selected_month_locator))

    def selected_month(self):
        return self.datepicker.find_element_by_xpath(self.selected_month_locator)

    def month_prev_button(self):
        return self.datepicker.find_element_by_xpath(self.month_prev_button_locator)

    def month_next_button(self):
        return self.datepicker.find_element_by_xpath(self.month_next_button_locator)

    def is_calender_visible(self):
        return self.is_element_visible((By.XPATH, self.calender_locator))

    def day_button(self, value):
        return self.datepicker.find_element_by_xpath(self.day_button_locator.replace('{day}', value))

    def is_hour_selector_visible(self):
        return self.is_element_visible((By.XPATH, self.hour_selector_locator))

    def hour_selector(self):
        return Select(self.datepicker.find_element_by_xpath(self.hour_selector_locator))

    def is_minute_selector_visible(self):
        return self.is_element_visible((By.XPATH, self.minute_selector_locator))

    def minute_selector(self):
        return Select(self.datepicker.find_element_by_xpath(self.minute_selector_locator))

    def is_select_button_visible(self):
        return self.is_element_visible((By.XPATH, self.select_button_locator))

    def select_button(self):
        return self.datepicker.find_element_by_xpath(self.select_button_locator)

    def get_month_position(self, month):
        return self.months.index(month) + 1