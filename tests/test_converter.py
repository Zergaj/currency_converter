import pytest


@pytest.mark.parametrize('def_testdata',
                         [['100', 'RUB', 'USD', 'card', 'to_account', 'internet_bank', 'no_package', 'current']])
def test_smoke_check(base, def_testdata):
    base.open_converter_page()
    assert base.is_converter_page_loaded()
    base.close_rules_panel()

    assert base.is_current_amount(def_testdata[0])
    assert base.is_selected_currency_from(def_testdata[1])
    assert base.is_selected_currency_to(def_testdata[2])
    assert base.is_selected_source(def_testdata[3])
    assert base.is_selected_receiving(def_testdata[4])
    assert base.is_selected_exchange_way(def_testdata[5])
    assert base.is_selected_pack_service(def_testdata[6])
    assert base.is_selected_converter_date(def_testdata[7])
    base.press_show_button()
    assert base.is_result_block_appeared()

    base.press_print_link()
    assert base.is_print_popup_opened()
    base.close_print_popup()
    assert base.is_print_popup_closed()

    base.press_quotation_popup_link()
    assert base.is_quotation_popup_opened()
    base.close_quotation_popup()
    assert base.is_quotation_popup_closed()


def test_currency_exchange_converter(base, testdata):
    base.open_converter_page()
    assert base.is_converter_page_loaded()
    base.close_rules_panel()

    base.enter_amount_value(testdata[0])
    base.select_currency_from(testdata[1])
    base.select_currency_to(testdata[2])
    base.select_source(testdata[3])
    base.select_receiving(testdata[4])
    base.select_exchange_way(testdata[5])
    base.select_pack_service(testdata[6])
    base.select_converter_date(testdata[7])

    base.press_show_button()
    assert base.is_result_block_appeared()
    assert base.check_result(testdata[8])


@pytest.mark.parametrize('data',
                         [['cash', 'to_account', 'cashless', 'branch_bank', 'internet_bank', 'atm']])
def test_check_radio_values_for_cash_source(base, data):
    base.open_converter_page()
    assert base.is_converter_page_loaded()
    base.close_rules_panel()

    base.select_source(data[0])

    assert base.is_selected_receiving(data[1])
    assert base.is_receiving_inactive(data[2])
    assert base.is_selected_exchange_way(data[3])
    assert base.is_exchange_way_inactive(data[4])
    assert base.is_exchange_way_inactive(data[5])
