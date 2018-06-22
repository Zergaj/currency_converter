from selenium.webdriver.support.ui import Select
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
        return self.is_element_visible(self.year_selector_locator)

    def year_selector(self):
        return self.element(self.year_selector_locator)

    def is_selected_month_visible(self):
        return self.is_element_visible(self.selected_month_locator)

    def selected_month(self):
        return self.element(self.selected_month_locator)

    def month_prev_button(self):
        return self.element(self.month_prev_button_locator)

    def month_next_button(self):
        return self.element(self.month_next_button_locator)

    def is_calender_visible(self):
        return self.is_element_visible(self.calender_locator)

    def day_button(self, value):
        return self.element(self.day_button_locator.replace('{day}', value))

    def is_hour_selector_visible(self):
        return self.is_element_visible(self.hour_selector_locator)

    def hour_selector(self):
        return Select(self.element(self.hour_selector_locator))

    def is_minute_selector_visible(self):
        return self.is_element_visible(self.minute_selector_locator)

    def minute_selector(self):
        return Select(self.element(self.minute_selector_locator))

    def is_select_button_visible(self):
        return self.is_element_visible(self.select_button_locator)

    def select_button(self):
        return self.element(self.select_button_locator)

    def get_month_position(self, month):
        return self.months.index(month) + 1