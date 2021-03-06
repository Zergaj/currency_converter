from _pytest.fixtures import fixture
from selenium import webdriver
from model.application import Application
import os


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="browser type")
    parser.addoption("--base_url", action="store", default="http://www.sberbank.ru/ru/quotes/converter", help="base URL")
    parser.addoption("--path", action="store", default="chromedriver", help="path to browser")
    parser.addoption("--path_to_test_data", action="store", default=None, help="path to test data file")


# MAIN FIXTURES
@fixture(scope="session")
def browser_type(request):
    return request.config.getoption("--browser")


@fixture(scope="session")
def base_url(request):
    return request.config.getoption("--base_url")


@fixture(scope="session")
def path(request):
    return request.config.getoption("--path")


@fixture(scope="session")
def base(browser_type, base_url, path):
    driver = None
    if browser_type == "firefox":
        driver = webdriver.Firefox(path)
    elif browser_type == "chrome":
        driver = webdriver.Chrome(path)
    driver.maximize_window()
    yield Application(driver, base_url)
    driver.close()


def pytest_generate_tests(metafunc):
    if 'testdata' in metafunc.fixturenames:
        lines = []
        with open(get_path_to_csv(metafunc)) as f:
            try:
                while True:
                    line = next(f).rstrip('\n').split(',')
                    lines.append(line)
            except StopIteration:
                pass
        metafunc.parametrize('testdata', lines)


def get_path_to_csv(metafunc):
    path_to_csv = metafunc.config.getoption('path_to_test_data')
    if not path_to_csv:
        path_to_csv = os.path.join(os.path.realpath('.'), 'test_data.csv')
    return path_to_csv
